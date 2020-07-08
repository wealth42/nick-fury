require("dotenv").config()

var express = require("express");
var app = express();
var mongoose = require("mongoose");
var bodyParser = require("body-parser");
var cookieParser = require("cookie-parser");
var cors = require("cors");

//================ MY ROUTES ==================================================================================== 
const authRoutes = require("./routes/auth");
const userRoutes = require("./routes/user");

//=============== CONNECTING TO DATABASE ===================
mongoose
    .connect(process.env.DATABASE ,{
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true
})
.then(() => {
    console.log("DB CONNECTED")
})

//========================= MIDDLEWARES ======================

app.use(bodyParser.json());
app.use(cookieParser());
app.use(cors());

// ==================== ROUTES =============================
app.use("/api" , authRoutes);
app.use("/api" , userRoutes);

// ================ PORT AND SERVER ======================================================================

var port = process.env.PORT || 8000
app.listen(port, () => {
    console.log(`server is running at ${port}`);
});