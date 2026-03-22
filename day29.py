#1st Exp

'''1. Install Node.js from https://nodejs.org
2. Open a terminal and create a project folder, e.g., hello-express
3. Initialize a Node.js project: npm init -y
4. Install Express.js: npm install express
5. Create app.js file and add the below code.
// app.js
const express = require('express');
const app = express();
// Define a route for the root URL
app.get('/', (req, res) => {
 res.send('Hello World');
});
// Start the server on port 3000
const PORT = 3000;
app.listen(PORT, () => {
console.log(`Server is running on http://localhost:${PORT}`);
});'''


#2 Exp

'''index.html
<!DOCTYPE html>
<html lang = "en">
<head>
<meta charset = "UTF-8">
<title> My Form </title>
<style>
a{
font-size: 40px;
}
</style>
</head>
<body align='center'>
<a href="./registration.html">Register</a>
<br>
<a href="./login.html">Login</a>
</body>
</html>
registration.html
<!DOCTYPE html>
<html lang = "en">
<head>
<meta charset = "UTF-8">
<title> My Form </title>
<style>
#mylink{
font-size: 25px;
}
</style>
</head>
<body align='center'>
<header>
<h1>Register</h1>
</header>
<form action="/register" method="POST">
<fieldset>
<label>Username</label>
<input type ="text" id = 'username' name="username" placeholder="maverick" required>
<br><br>
<label>Email ID</label>
<input type ="email" id = 'email' name="email" placeholder="abc@example.com" required>
<br><br>
<label>Password</label>
<input type="password" id = "password" name="password" required>
<br><br>
<button type ="reset">Reset</button>
<button type ="submit">Submit</button>
</fieldset>
</form>
<br><br>
<a id="mylink" href="./login.html">login</a>
</body>
</html>
login.html
<!DOCTYPE html>
<html lang = "en">
<head>
<meta charset = "UTF-8">
<title> My Form </title>
<style>
#mylink{
font-size: 25px;
}
</style>
</head>
<body align='center'>
<header>
<h1>Login</h1>
</header>
<form action="/login" method="POST">
<fieldset>
<label>Email ID</label>
<input type ="email" id = 'email' name="email" placeholder="abc@example.com" required>
<br><br>
<label>Password</label>
<input type="password" id = "password" name="password" required>
<br><br>
<button type ="reset">Reset</button>
<button type ="submit">Submit</button>
</fieldset>
</form>
<br><br>
<a id="mylink" href="./registration.html">register</a>
</body>
</html>
app.js
const express = require('express');
const http = require('http');
const bcrypt = require('bcrypt');
const path = require("path");
const bodyParser = require('body-parser');
const users = require('./data').userDB;
const app = express();
const server = http.createServer(app);
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname,'./public')));
app.get('/',(req,res) => {
res.sendFile(path.join(__dirname,'./public/index.html'));
});
app.post('/register', async (req, res) => {
try{
let foundUser = users.find((data) => req.body.email === data.email);
if (!foundUser) {
let hashPassword = await bcrypt.hash(req.body.password, 10);
let newUser = {
id: Date.now(),
username: req.body.username,
email: req.body.email,
password: hashPassword,
};
users.push(newUser);
console.log('User list', users);
res.send("<div align ='center'><h2>Registration successful</h2></div><br><br><div
align='center'><a href='./login.html'>login</a></div><br><br><div align='center'><a
href='./registration.html'>Register another user</a></div>");
} else {
res.send("<div align ='center'><h2>Email already used</h2></div><br><br><div
align='center'><a href='./registration.html'>Register again</a></div>");
}
} catch{
res.send("Internal server error");
}
});
app.post('/login', async (req, res) => {
try{
let foundUser = users.find((data) => req.body.email === data.email);
if (foundUser) {
let submittedPass = req.body.password;
let storedPass = foundUser.password;
const passwordMatch = await bcrypt.compare(submittedPass, storedPass);
if (passwordMatch) {
let usrname = foundUser.username;
res.send(`<div align ='center'><h2>login successful</h2></div><br><br><br><div align
='center'><h3>Hello ${usrname}</h3></div><br><br><div align='center'><a
href='./login.html'>logout</a></div>`);
} else {
res.send("<div align ='center'><h2>Invalid email or password</h2></div><br><br><div align
='center'><a href='./login.html'>login again</a></div>");
}
}
else {
let fakePass = `$2b$$10$ifgfgfgfgfgfgfggfgfgfggggfgfgfga`;
await bcrypt.compare(req.body.password, fakePass);
res.send("<div align ='center'><h2>Invalid email or password</h2></div><br><br><div
align='center'><a href='./login.html'>login again<a><div>");
}
} catch{
res.send("Internal server error");
}
});
server.listen(3000, function(){
console.log("server is listening on port: 3000");
});
data.js
const userDB = [];
module.exports = { userDB };
Execution Steps:
1. Open a terminal and create a project folder, e.g., login-express
2. Initialize a Node.js project: npm init -y
3. Install Express.js: npm install express, bcrypt and body-parser.
'''

#3 exp

'''Create fileOperations.js file and add the below code.
const fs = require('fs');
const readline = require('readline');
const rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout
});
// Function to show menu
function showMenu() {
 console.log("\n===== FILE OPERATIONS MENU =====");
 console.log("1. Write/Create File");
 console.log("2. Read File");
 console.log("3. Append to File");
 console.log("4. Rename File");
 console.log("5. Delete File");
 console.log("6. Exit");
 rl.question("Enter your choice (1-6): ", handleChoice);
}
// Function to handle user choice
function handleChoice(choice) {
 switch (choice) {
 case '1': // WRITE FILE
 rl.question("Enter filename: ", (file) => {
 rl.question("Enter content to write: ", (content) => {
 fs.writeFile(file, content, (err) => {
 if (err) console.log("Error:", err);
 else console.log("File created and written successfully!");
 showMenu();
 });
 });
 });
 break;
 case '2': // READ FILE
 rl.question("Enter filename to read: ", (file) => {
 fs.readFile(file, "utf8", (err, data) => {
 if (err) console.log("Error:", err);
 else console.log("\nFile content:\n" + data);
 showMenu();
 });
 });
 break;
 case '3': // APPEND FILE
 rl.question("Enter filename: ", (file) => {
 rl.question("Enter content to append: ", (content) => {
 fs.appendFile(file, content, (err) => {
 if (err) console.log("Error:", err);
 else console.log("Content appended successfully!");
 showMenu();
 });
 });
 });
 break;
 case '4': // RENAME FILE
 rl.question("Enter old filename: ", (oldName) => {
 rl.question("Enter new filename: ", (newName) => {
 fs.rename(oldName, newName, (err) => {
 if (err) console.log("Error:", 
 else console.log("File renamed successfully!");
 showMenu();
 });
 });
 });
 break;
 case '5': // DELETE FILE
 rl.question("Enter filename to delete: ", (file) => {
 fs.unlink(file, (err) => {
 if (err) console.log("Error:", err);
 else console.log("File deleted successfully!");
 showMenu();
 });
 });
 break;
 case '6': // EXIT
 console.log("Exiting program...");
 rl.close();
 break;
 default:
 console.log("Invalid choice! Please try again.");
 showMenu();
 }
}
// Start menu
showMenu();
2. Save the program
3. Open terminal
4. Run: node fileOperations.js'''

#4 exp

'''Execution Steps:
1. Create readParams.js file and add the below code.
const http = require("http");
const url = require("url");
http.createServer(function (req, res) {
 // Parse the URL and extract query parameters
 const q = url.parse(req.url, true).query;
 // Prepare HTML output
 res.writeHead(200, { "Content-Type": "text/html" });
 res.write("<h2>Form Data Received</h2>");
 if (Object.keys(q).length === 0) {
 res.write("<p>No query string data found!</p>");
 } else {
 res.write("<ul>");
 for (let key in q) {
 res.write(`<li><strong>${key}</strong>: ${q[key]}</li>`);
 }
 res.write("</ul>");
 
 }
 res.end();
}).listen(3000);
console.log("Server running at http://localhost:3000/");
5. Save the program
6. Open terminal
7. Run: node readParams.js'''

#5 exp

'''index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Food Delivery</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="container">
<h1> Food Delivery</h1>
<h2>Select Your Favorite Food</h2>
<div class="food-box">
<img src="/images/pizza.jpg" alt="Pizza">
<h3>Pizza</h3>
<form action="/order" method="GET">
<input type="hidden" name="food" value="Pizza">
<button type="submit">Order Pizza</button>
</form>
</div>
<div class="food-box">
<img src="/images/biryani.jpg" alt="Biryani">
<h3>Biryani</h3>
<form action="/order" method="GET">
<input type="hidden" name="food" value="Biryani">
<button type="submit">Order Biryani</button>
</form>
</div>
<div class="food-box">
<img src="/images/burger.jpg" alt="Burger">
<h3>Burger</h3>
<form action="/order" method="GET">
<input type="hidden" name="food" value="Burger">
<button type="submit">Order Burger</button>
</form>
</div>
</div>
</body>
</html>
style.css
body {
font-family: Arial, sans-serif;
background: #f7f7f7;
margin: 0;
padding: 0;
}
.container {
width: 80%;
margin: auto;
text-align: center;
padding: 20px;
}
h1 {
color: #ff5733;
font-size: 40px;
}
.food-box {
display: inline-block;
width: 280px;
background: white;
margin: 15px;
padding: 15px;
border-radius: 12px;
box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
.food-box img {
width: 100%;
height: 180px;
border-radius: 10px;
}
.food-box h3 {
margin: 10px 0;
}
button {
background: #28a745;
color: white;
padding: 10px 18px;
border: none;
border-radius: 6px;
cursor: pointer;
font-size: 16px;
}
button:hover {
background: #218838;
}
server.js
//create node server with expressjs
const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
//add style.css file present in the current directory
app.use(express.static(path.join(__dirname, '')));
app.use(express.urlencoded({ extended: true }));
// Route to serve the HTML file
app.get('/', (req, res) => {
res.sendFile(path.join(__dirname, 'index.html'));
});
// Route to handle order requests
app.get('/order', (req, res) => {
const item = req.query.food;
res.send(`Your order for a ${item} has been received!`);
});
// Start the server
app.listen(port, () => {
console.log(`Server is running at http://localhost:${port}`);
});
Execution Steps:
1. npm init -y
2. npm i express
3. node server.js'''

#6 & 7 

'''mongoBasic.js
const { MongoClient } = require("mongodb");
// MongoDB URL
const url = "mongodb://127.0.0.1:27017";
const client = new MongoClient(url);
// Database Name
const dbName = "collegeDB";
async function run() {
 try {
 // Connect to MongoDB
 await client.connect();
 console.log("Connected successfully to MongoDB");
 // Create / Switch Database
 const db = client.db(dbName);
 // Create Collection
 const students = db.collection("students");
 // INSERT ONE
 await students.insertOne({
 rollNo: 1,
 name: "Ravi",
 branch: "CSE",
 marks: 85
 });
 console.log("One student inserted");
 // INSERT MANY
 await students.insertMany([
 { rollNo: 2, name: "Sita", branch: "IT", marks: 78 },
 { rollNo: 3, name: "Kiran", branch: "CSE", marks: 90 },
 { rollNo: 4, name: "Anu", branch: "ECE", marks: 72 }
 ]);
 console.log("Multiple students inserted");
 // READ DATA
 const allStudents = await students.find().toArray();
 console.log("Student Records:");
 console.log(allStudents);
 // UPDATE ONE
 await students.updateOne(
 { rollNo: 1 },
 { $set: { marks: 88 } }
 );
 console.log("One student updated");
 // DELETE ONE
 await students.deleteOne({ rollNo: 4 });
 console.log("One student deleted");
 } catch (err) {
 console.error(err);
 } finally {
 // Close connection
 await client.close();
 }
}
// Call function
run();
Execution Steps:
1. node mongoBasic.js'''

'''const mongoose = require("mongoose");
const studentSchema = new mongoose.Schema({
rollNo: Number,
studentName: String,
branch: String,
year: Number,
cgpa: Number
});
module.exports = mongoose.model("Student", studentSchema);
Place .html files inside public folder
add.html
<h2>Add Student</h2>
<form id="addForm">
Roll No: <input id="rollNo"><br>
Student Name: <input id="studentName"><br>
Branch: <input id="branch"><br>
Year: <input id="year"><br>
CGPA: <input id="cgpa"><br>
<button>Add</button>
</form>
<script src="script.js"></script>
edit.html
<h2>Edit Student</h2>
<form id="editForm">
Roll No: <input id="rollNo"><br>
Student Name: <input id="studentName"><br>
Branch: <input id="branch"><br>
Year: <input id="year"><br>
CGPA: <input id="cgpa"><br>
<button>Update</button>
</form>
<script src="script.js"></script>
index.html
<!DOCTYPE html>
<html>
<body>
<h2>Student List</h2>
<a href="add.html">Add Student</a>
<table border="1" id="table">
<tr>
<th>Roll No</th><th>Student Name</th><th>Branch</th>
<th>Year</th><th>CGPA</th><th>Actions</th>
</tr>
</table>
<script src="script.js"></script>
</body>
</html>
script.js
const addForm = document.getElementById("addForm");
const editForm = document.getElementById("editForm");
if(document.getElementById("table")){
fetch("/students").then(r=>r.json()).then(data=>{
table.innerHTML += data.map(s=>`
<tr>
<td>${s.rollNo}</td>
<td>${s.studentName}</td>
<td>${s.branch}</td>
<td>${s.year}</td>
<td>${s.cgpa}</td>
<td>
<a href="edit.html?id=${s._id}">Edit</a>
<button onclick="del('${s._id}')">Delete</button>
</td>
</tr>`).join("");
});
}
function del(id){
fetch("/students/"+id,{method:"DELETE"}).then(()=>location.reload());
}
if(addForm){
addForm.onsubmit=e=>{
e.preventDefault();
fetch("/students",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
rollNo:rollNo.value,
studentName:studentName.value,
branch:branch.value,
year:year.value,
cgpa:cgpa.value
})
}).then(()=>location.href="/");
};
}
if(editForm){
const id=new URLSearchParams(location.search).get("id");
fetch("/students/"+id).then(r=>r.json()).then(s=>{
rollNo.value=s.rollNo;
studentName.value=s.studentName;
branch.value=s.branch;
year.value=s.year;
cgpa.value=s.cgpa;
});
editForm.onsubmit=e=>{
e.preventDefault();
fetch("/students/"+id,{method:"PUT",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
rollNo:rollNo.value,
studentName:studentName.value,
branch:branch.value,
year:year.value,
cgpa:cgpa.value
})
}).then(()=>location.href="/");
};
}
server.js
const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const Student = require("./models/Student");
const app = express();
mongoose.connect("mongodb://127.0.0.1:27017/collegeDB");
app.use(bodyParser.json());
app.use(express.static("public"));
app.post("/students", async (req, res) => {
const student = await Student.create(req.body);
res.json(student);
});
app.get("/students", async (req, res) => {
res.json(await Student.find());
});
app.get("/students/:id", async (req, res) => {
res.json(await Student.findById(req.params.id));
});
app.put("/students/:id", async (req, res) => {
await Student.findByIdAndUpdate(req.params.id, req.body);
res.sendStatus(200);
});
app.delete("/students/:id", async (req, res) => {
await Student.findByIdAndDelete(req.params.id);
res.sendStatus(200);
});
app.listen(3000, ()=>console.log("http://localhost:3000"));
Execution: node server.js'''

#7 exp 

'''To perform Count, Limit, Sort, and Skip operations on a MongoDB collection and observe how these
commands are used to manage and retrieve data efficiently.
Theory
Querying data in MongoDB is done using methods that allow filtering, retrieving, and structuring the
results. Among these, Count, Limit, Sort, and Skip are important cursor operations that help in
pagination, filtering, data analytics, and optimized data display.
COUNT Documents
Count is used to determine the total number of documents available in a collection or based on a given
filtercondition.
It is useful to calculate dataset size, number of matching records, and statistical analysis.
Count how many documents are present in a collection: db.students.count()
Count based on a filter (example: CSE students): db.students.count({ dept: "CSE" })
LIMIT – Restrict Number of Documents
limit() is used to restrict the number of documents returned by a query.
This is helpful when displaying small chunks of data at a time (pagination), reducing data transfer, and
improving performance.
Shows only first 2 records: db.students.find().limit(2)
SORT – Sort the Results
sort() rearranges the resulting documents in ascending (1) or descending (-1) order based on a selected
field. Sorting is useful in ranking, leaderboard display, alphabetical listing, and analytics.
Sort alphabetically by name (ascending - A–Z): db.students.find().sort({ name: 1 })
Sort marks highest to lowest (descending): db.students.find().sort({ marks: -1 })
SKIP – Skip Records
skip() is used to ignore a specified number of documents from the beginning of the result set.
It is mainly used for pagination along with limit() to fetch data page-wise.
Skip first 2 documents and show remaining: db.students.find().skip(2)
Combine – Sort + Limit + Skip
To display specific chunks of sorted data, multiple operations can be combined:
Show next 2 students after top scorer: db.students.find().sort({ marks: -1 }).skip(1).limit(2)'''