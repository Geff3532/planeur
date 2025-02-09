const cors = require('cors');
const express = require('express');
const mysql = require('mysql');

const app = express();

//const corsOptions ={
  //  origin:'http:localhost:3000', 
    //credentials:true,            //access-control-allow-credentials:true
    //optionSuccessStatus:200
//}
app.use(cors());

app.get('/api/[0-9]{11}', function (req, res) 
{
    res.setHeader("Access-Control-Allow-Origin", "*");
    sql(req.originalUrl.split('/')[2]).then(json => 
    {
        return res.status(200).contentType('application/json').send(json);
    }
    ).catch((status,err) => 
    {
        return res.status(status).send(err);
    });
});

app.listen(3000, () => console.log('Votre app est disponible sur localhost:3000 !'));

const sql = (id) => 
{
    return new Promise((resolve, reject) => 
    {
        let connection = mysql.createConnection({
            host     : 'localhost',
            user     : 'root',
            password : '',
            database : 'test',
            charset  : 'utf8'
        });
        
        connection.connect( (err) => 
        {
            if (err) 
            {
                console.log('Error connecting to mysql base: ' + err.stack);
                return reject(500,'Error 500 => Internal Server Error : Failure connection to database');
            }
        });

        connection.query(
        {
            sql: 'SELECT * FROM `acs_planche` WHERE `id` = ?',
            timeout: 10000, // 10s
            values: [id]
        }, (error, results, fields) => 
        {
            if (error != null) 
            
            {
                console.log(error);
                return reject(500,'Internal Server Error : Failure request to databse sql');
            }
            if (results == undefined || results[0] == undefined) return reject(400,'Error 400 => Bad request : No data corresponding to this id');
            let json = JSON.stringify(results[0],null,2);
            if (json == {}) return reject(400,'Error 400 => Bad request : No data corresponding to this id');
            return resolve(json);
        });

        connection.end();
    });
}