export default (req, res, next) => {
    const userAgent = req.get("User-Agent");
    if (userAgent == "robot") {
        next();
    } else {
        console.log("forget to change user-agent");
        res.render("robot", { error: "🤖🤖🤖🤖🤖" });
    }
};
