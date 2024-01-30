const express = require("express");
const cors = require("cors");
const spawn = require("child_process").spawn //This allows me to use Python

const app = express();

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({limit: '100mb', extended: true}))
app.use((req, res, next) => {
	res.setHeader("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Methods", "POST, GET, PUT");
	res.header("Access-Control-Allow-Headers", "Content-Type");
	next();
})
app.options('*', cors())

//Uses the python summary file
app.post("/summary", (req, res) => {

	console.log("Has gotten here")
	let child;
	let wordCounter = req.body.text.split(" ").length
	let sum_vals = {
		1 : [30, 130], 
		2 : [100, 300],
		3 : [150, 400],
		4 : [200, 500]
	}
	let len = parseInt(req.body.length)
	
	if (len === 0)
	{
		child = spawn('python3', ['./pyAPI/bullet.py', req.body.text])
	}
	else
	{
		if(len === 1)
		{
			if (wordCounter >= sum_vals[1][0])
			{
				child = spawn('python3', ['./pyAPI/summarizer.py', req.body.text, sum_vals[1][0], sum_vals[1][1]] )
			}
			else{
				console.log("This sentence is too short to summarize.")
			}
		}
		else if (wordCounter >= sum_vals[req.body.length][0])
		{
			child = spawn('python3', ['./pyAPI/summarizer.py', req.body.text, sum_vals[len][0], sum_vals[len][1]] )
		}
		else
		{
			child = spawn('python3', ['./pyAPI/summarizer.py', req.body.text, sum_vals[len-1][0], sum_vals[len-1][1]] )
		}
	}
	
	child.stdout.on('data', (data)=>{
		console.log("stdout: ", Buffer.from(data.toString(), "hex").toString())
		res.send({summary: Buffer.from(data.toString(), "hex").toString()})
	})
	child.stderr.on('data', (data)=>{
		console.error("stderr: ", data.toString())
	})
	child.on('close', (code)=>{
		console.log('child process exited with code', code.toString())
	})
})

//Uses the python spellcheck file
app.post("/spellcheck", (req, res)=>{
	console.log(req.body)
	let child;
	child = spawn('python3', ['./pyAPI/spellchecker.py', req.body.text])


	child.stdout.on('data', (data)=>{
		console.log("stdout: ", data.toString())
		res.send({summary: Buffer.from(data.toString(), "hex").toString()})
	})
	child.stderr.on('data', (data)=>{
		console.error("stderr: ", data.toString())
	})
	child.on('close', (code)=>{
		console.log('child process exited with code', code.toString())
	})
})

//A get file that's uncommon to check if deployment is working well 
app.get("/", (req, res) => {
	res.send("Hello World! Sd'c iyeb qsbv BycoKceuy!");
});

//Voice file stuff. May or may not use in the future 
// app.post("/voice", (req, res)=>{
// 	console.log("in voice")
// 	console.log(req.body)
// 	let child;
// 	child = spawn('python3', ['./pyAPI/texttospeech.py', req.body.text])


// 	child.stdout.on('data', (data)=>{
// 		console.error("stdout: ", data.toString())
// 	})
// 	child.stderr.on('data', (data)=>{
// 		console.error("stderr: ", data.toString())
// 	})
// 	child.on('close', (code)=>{
// 		console.log('child process exited with code', code.toString())
// 	})
// })

const PORT = process.env.PORT || 3000;

app.listen(PORT,
    console.log(`Server started on port ${PORT}`)
);
