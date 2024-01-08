const Sequelize = require('sequelize')
const User = require('./user')
const Comment = require('./comment')

const env = process.env.NODE_ENV || 'development' //process.env.NODE_ENV 선언되어있으면 그 값, 아니면 config.json의 development을 이용
// mysql 연동하기 위한 정보가 설정된 파일
const config = require('../config/config')[env] 
const db = {}

const sequelize = new Sequelize(config.database, config.username, config.password, config)
db.sequelize = sequelize

// db에 등록 
db.User = User
db.Comment = Comment

// User 클래스의 initiate를 호출함 (초기화 준비해라)
User.initiate(sequelize)
Comment.initiate(sequelize)

User.associate(db)
Comment.associate(db)

module.exports = db 