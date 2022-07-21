import {createServer} from "http";
import {Server} from "socket.io";
import redis from "redis";

const httpServer = createServer();
const io = new Server(httpServer, {
    cors: {
        origin: '*',
        methods: ["GET", "POST"],
    }
});

var redisClient = redis.createClient({
    url: 'redis://redis:6379'
});

io.on("connection", (socket) => {
    console.log("user conected")
});

redisClient.subscribe("message")
redisClient.on('message', function (channel, message) {
    console.log(channel)
    let data = eval('(' + message + ')')

    io.emit('room'+data.room, data);
});


httpServer.listen(3000);
