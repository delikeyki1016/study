const express = require('express')
const User = require('../models/user')

const router = express.Router()

router.get('/', async (req, res, next) =>{
    try {
        const users = await User.findAll() // findAll()함수는 Sequelize에 포함된 함수이다. users는 셀렉트 해온 결과 데이터 
        res.render('sequelize', {users})
    } catch(err) {
        console.log(err)
        next(err)
    }
})

module.exports = router
