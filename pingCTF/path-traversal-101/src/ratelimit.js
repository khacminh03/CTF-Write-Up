import { rateLimit } from "express-rate-limit";

export default rateLimit({
    windowMs: 60 * 1000,
    limit: 200,
    standardHeaders: "draft-7",
    legacyHeaders: false,
});
