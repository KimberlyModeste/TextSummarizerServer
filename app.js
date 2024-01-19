const express = require("express");
const cors = require("cors");
const { decode } = require("punycode");
const { escape } = require("querystring");
const spawn = require("child_process").spawn
// let child = require("./child")

const app = express();

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({limit: '100mb', extended: true}))

app.post("/summary", (req, res) => {

	let child;
	let wordCounter = req.body.text.split(" ").length
	let sum_vals = {
		1 : [30, 130], 
		2 : [100, 300],
		3 : [150, 400],
		4 : [200, 500]
	}
	
	
	if (req.body.length === 0)
	{
		child = spawn('python', ['bullet.py', req.body.text])
	}
	else
	{
		if(req.body.length === 1)
		{
			if (wordCounter >= sum_vals[1][0])
			{
				child = spawn('python', ['summarizer.py', req.body.text, sum_vals[1][0], sum_vals[1][1]] )
			}
			else{
				console.log("This sentence is too short to summarize.")
			}
		}
		else if (wordCounter >= sum_vals[req.body.length][0])
		{
			child = spawn('python', ['summarizer.py', req.body.text, sum_vals[req.body.length][0], sum_vals[req.body.length][1]] )
		}
		else
		{
			child = spawn('python', ['summarizer.py', req.body.text, sum_vals[req.body.length-1][0], sum_vals[req.body.length-1][1]] )
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

app.get("/", (req, res) => {
	res.send("Hello World");
});

const PORT = process.env.PORT || 8080;

app.listen(PORT,
    console.log(`Server started on port ${PORT}`)
);
