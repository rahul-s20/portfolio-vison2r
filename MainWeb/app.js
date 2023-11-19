const express = require('express');
const dotend = require('dotenv').config();
const session = require('express-session');
const app = express();
app.use(express.json());

app.set('view engine', 'ejs')

app.use(express.urlencoded({ extended : false}));

//express middleware
app.use(
    session({
        secret: 'Rahulsecret',
        resave: true,
        saveUninitialized: true
    }));

app.use('/assets',express.static((__dirname + '/public')));

app.use('/', require('./routes/index'))

const port =process.env.PORT || 7000;
app.listen(port, console.log(`Server connected to port ${port}`));    