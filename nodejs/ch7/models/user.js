// 유저 모델을 정의하는 파일
// 모델이란 데이터를 구성하는 객체
// 클래스로 선언하는데, 시퀄라이저에게 어떻게 데이터베이스랑 매핑해야된다라는 정보를 설정해서
// 시퀄라이저는 ORM을 제공하고, ORM에 의해 데이터베이스 연동을 조금 더 편하게 할 수는 있지만,
// 최소한의 정보는 줘야 함. User 클래스이 데이터가 데이터베이스에 어떻게 매핑이 되어야하는지에 대한 정보 설정 

const Sequelize = require('sequelize')

class User extends Sequelize.Model { // Sequelize.Model을 상속받아서 User 클래스 생성
    // 어디선가 User 초기화를 위해서 호출
    // DB에 테이블 생성하기 위한 객체 생성(초기화) 
    static initiate(sequelize) {
        User.init({
            name: {
                type: Sequelize.STRING(20),
                allowNull: false,
                unique: true
            },
            age: {
                type: Sequelize.INTEGER.UNSIGNED,
                allowNull: false,
            },
            married: {
                type: Sequelize.BOOLEAN,
                allowNull: false,
            },
            comment: {
                type: Sequelize.TEXT,
                allowNull: true,
            },
            create_at: {
                type: Sequelize.DATE,
                allowNull: false,
                defaultValue: Sequelize.NOW
            }
        },{
            sequelize, //표현 형식에 대한 옵션 정의
            timestamps: false,
            underscored: false,
            modelName: 'User',
            tableName: 'users',
            paranoid: false,
            charset: 'utf8',
            collate: 'utf8_general_ci'
        })
    }
    // 이 모델과 다른 모델이 관계가 있다면, 관계 설정을 해야함 
    // 결국 DB적으로 보면 foreign Key와 같은 설정 
    static associate(db){
        // User - Comment : 1: n
        db.User.hasMany(db.Comment, {foreignKey: 'commenter', sourceKey: 'id'})
    }
}

module.exports = User