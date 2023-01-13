import React from "react";

const User = ({userData}) => {
    return (
        <tr>
            <td>{userData.name}</td>
            <td>{userData.email}</td>
        </tr>
    )
}

const UserList = () => {

    const users = [
        {email: 'kwon@gmail.com', name: '배중권'},
        {email: 'sick@gmail.com', name: '배민식'},
        {email: 'yeon@gmail.com', name: '배중연'},
        {email: 'ok@gmail.com', name: '김인옥'},
    ];

    return (
        <table>
            <thead>
                <tr>
                    <th>이름</th>
                    <th>이메일</th>
                </tr>
            </thead>
            <tbody>
                {users.map(user => <User userData={user} />)}
            </tbody>
        </table>
    )
}

export default UserList;