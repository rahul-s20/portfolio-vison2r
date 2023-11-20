const axios = require('axios');
const ErrorHandler = require('../utils/ErrorHandler');


const api = axios.create({
    baseURL: process.env.BASE_URL || "http://localhost:3030",
});

const aboutMe = async(req, res) =>{
    try{
        body = {
            email: 'rahulsarkar334@gmail.com'
          }
        data = await api.get('/profile/me', {data: body})
        full_res = data.data.data
        console.log(full_res.skill_sets_mod[1])
        // for(var i=0; i<=full_res.skill_sets_mod.length; i++){
        //     console.log("data.data.data")
        //     console.log(full_res.skill_sets_mod[i])
        // }
        res.render('index', {all_data: data.data.data})
    }
    catch(e){
        return next(new ErrorHandler(`${e}`, 400));
    }
}

module.exports = {aboutMe}
   