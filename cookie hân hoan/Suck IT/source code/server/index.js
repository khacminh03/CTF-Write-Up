const fs = require('fs');
const FLAG = fs.readFileSync('/flag.txt');
const httpServer = require("http").createServer();
const Redis = require("ioredis");
const redisClient = new Redis();
const io = require("socket.io")(httpServer, {
  cors: {
    origin: "*"
  },
  adapter: require("socket.io-redis")({
    pubClient: redisClient,
    subClient: redisClient.duplicate(),
  }),
});

const crypto = require("crypto");
const randomId = () => crypto.randomBytes(16).toString("hex");

const { RedisSessionStore } = require("./sessionStore");
const sessionStore = new RedisSessionStore(redisClient);

const { RedisMessageStore } = require("./messageStore");
const messageStore = new RedisMessageStore(redisClient);

io.use(async (socket, next) => {
  const sessionID = socket.handshake.auth.sessionID;
  if (sessionID) {
    const session = await sessionStore.findSession(sessionID);
    if (session) {
      socket.sessionID = sessionID;
      socket.userID = session.userID;
      socket.username = session.username;
      return next();
    }
  }
  const username = socket.handshake.auth.username;
  if (!username) {
    return next(new Error("invalid username"));
  }
  socket.sessionID = randomId();
  socket.userID = randomId();
  socket.username = username;
  next();
});

// init DB
(async () => {
  const [sessions,adminSession] = await Promise.all([
    sessionStore.findAllSessions(),
    sessionStore.findSessionsByUserID("ADMIN"),
  ]);
  if (sessions.length === 0){
    sessionStore.saveSession(randomId(), {
      userID: 'thangbanthan',
      username: 'Bạn thân',
      connected: true,
    });
  
    sessionStore.saveSession(randomId(), {
      userID: 'nguoiyeudonphuong',
      username: 'Crush',
      connected: true,
    });
  
    sessionStore.saveSession(randomId(), {
      userID: 'buctuong',
      username: 'Bức tường',
      connected: true,
    });
  
    sessionStore.saveSession(randomId(), {
      userID: 'nguoiyeucuaADMIN',
      username: 'Người yêu của Admin',
      connected: true,
    });
    const adminID = randomId();
    // console.log(adminID);
    sessionStore.saveSession(adminID, {
      userID: 'ADMIN',
      username: 'Admin',
      connected: false,
    });
  }
  // else{
  //   console.log(adminSession)
  // }

})();


io.on("connection", async (socket) => {
  // persist session
  sessionStore.saveSession(socket.sessionID, {
    userID: socket.userID,
    username: socket.username,
    connected: true,
  });

  // emit session details
  socket.emit("session", {
    sessionID:socket.sessionID,
    userID: socket.userID,
  });

  // join the "userID" room
  socket.join(socket.userID);

  // fetch existing users
  const users = [];
  const [messages, sessions] = await Promise.all([
    messageStore.findMessagesForUser(socket.userID),
    sessionStore.findAllSessions(),
  ]);
  const messagesPerUser = new Map();
  messages.forEach((message) => {
    const { from, to } = message;
    const otherUser = socket.userID === from ? to : from;
    if (messagesPerUser.has(otherUser)) {
      messagesPerUser.get(otherUser).push(message);
    } else {
      messagesPerUser.set(otherUser, [message]);
    }
  });
  sessions.forEach((session) => {
    users.push({
      userID: session.userID,
      username: session.username,
      connected: session.connected,
      messages: messagesPerUser.get(session.userID) || [],
    });
  });
  socket.emit("users", users);
  // notify existing users
  socket.broadcast.emit("user connected", {
    userID: socket.userID,
    username: socket.username,
    connected: true,
    messages: [],
  });

  // forward the private message to the right recipient (and to other tabs of the sender)
  socket.on("private message", ({ content, to }) => {
    const message = {
      content,
      from: socket.userID,
      to,
    };

    switch(to){
      case "thangbanthan":
        message.content = "T đang bận, 5p sau t trả lời. Sau 5p, k thấy trả lời thì xem lại tn này.";
        message.from = to;
        message.to = socket.userID

        socket.emit("private message", message);
        break;
      case "nguoiyeudonphuong":
        const cachcrushtraloi = ['uh','ok','um','seen','seen','seen','seen','seen','seen','seen','seen']
        var reg1 = /n\s*?g\s*?.\s*?.\s*?i\s*?y?\s*?.\s*?u/g
        var reg2 = /b\s*?.\s*?n\s*?g?\s*?.\s*?i/g
        message.content=cachcrushtraloi[Math.floor(Math.random() * cachcrushtraloi.length)];
        
        if(content.match(reg1)||content.match(reg2)){ "chê"; }
        message.from = to;
        message.to = socket.userID

        socket.emit("private message", message);
        break;
      case "nguoiyeucuaADMIN":
        if(socket.userID !== "ADMIN"){
          message.content="I do not associate with n.....on-Admin";
        }else{
          message.content="Đêm qua em tuyệt lắm: \n"+FLAG;
        }
        message.from = to;
        message.to = socket.userID
        socket.emit("private message", message);
        break;
      case "buctuong":
        break;
      default:
        socket.to(to).to(socket.userID).emit("private message", message);
        messageStore.saveMessage(message);
    }

  });

  // admin force any user to disconnect
  socket.on("force disconnect",async (userID,secretKey)=>{
    // check valid account
    if (secretKey !== "574a94b04f303f5663e833b883cd2b23"){
      socket.emit("This secret key is wrong.")
    }
    else{
    const targetSocket = await sessionStore.findSessionsByUserID(userID);
    const matchingSockets = await io.in(targetSocket.userID).allSockets();
    const isDisconnected = matchingSockets.size === 0;
    if (isDisconnected) {
      // notify other users
      socket.broadcast.emit("user disconnected", targetSocket.userID);
      // update the connection status of the session
      socket.emit(targetSocket.sessionID);
      sessionStore.saveSession(targetSocket.sessionID, {
        userID: targetSocket.userID,
        username:targetSocket.username,
        connected: false,
      });
    }};
  });

  // notify users upon disconnection
  socket.on("disconnect", async () => {
    const matchingSockets = await io.in(socket.userID).allSockets();
    const isDisconnected = matchingSockets.size === 0;
    if (isDisconnected) {
      // notify other users
      socket.broadcast.emit("user disconnected", socket.userID);
      // update the connection status of the session
      sessionStore.saveSession(socket.sessionID, {
        userID: socket.userID,
        username: socket.username,
        connected: false,
      });
    }
  });
});

const PORT = process.env.PORT || 5000;
httpServer.listen(PORT, () =>{
  console.log(`server listening at http://localhost:${PORT}`);
});