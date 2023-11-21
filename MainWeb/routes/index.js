const express = require('express');
const router = express.Router();
const {aboutMe} = require('../controllers/profileController')





router.get('/about', aboutMe);
router.get('/detailsToFill', (req, res)=>{
    res.render('input_form')
});
// router.get('/home',  homecontroll.getPosts );
// router.get('/signout', ensureAuthenticated, usercontroll.signOut);
// router.get('/edit/:id', ensureAuthenticated, postcontroll.getAll)

// router.get('/delete/:id', ensureAuthenticated, postcontroll.deletePost)

// router.use('/game',express.static('public/fb.html'))



module.exports = router;