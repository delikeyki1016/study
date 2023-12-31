const express = require('express')
const User = require('../models/user')
const Comment = require('../models/comment')

const router = express.Router()

router.route('/')
    .get(async (req, res, next) => {
        try {
            const users = await User.findAll() // User의 *을 셀렉트하고, 
            res.json(users) // res에 데이터를 보냄
        } catch(err) {
            console.log(err)
            next(err)
        }
    })
    .post(async (req, res, next) => { // 새로운 유저 저장
        try {
            const user = await User.create({
                name: req.body.name,
                age: req.body.age,
                married: req.body.married
            })
            console.dir(user)
            res.status(200).json(user)
        } catch(err) {
            console.log(err)
            next(err)
        }
    })

// 특정 유저가 쓴 글만 보기 위해서.
router.get('/:id/comments', async (req, res, next) => {
    try{
        const comments = await Comment.findAll({
            include: {
                model:User,
                where: {id:req.params.id}
            }
        })
        res.json(comments)
        }catch(err){
            console.log(err)
            next(err)
        }
    })

module.exports = router