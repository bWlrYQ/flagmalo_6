const puppeteer = require('puppeteer');
const fs = require('fs');

let content = "";
fs.readFile(process.argv[2], 'utf8', (err,data) => {
	if(err){
		console.error(err);
		return;
	}
	console.log("querying : "+data);
	browse(data);
});

const cookie={
  "name":"ADMIN_COOKIE",
  "value":"e09c4bc5382d1e56f45c72208caae1a9", 
  "url":"https://straighttohell.chall.flagmalo.fr/", //changer par l'URL du chall ou l'IP + port
  "secure":false,
  "httpOnly":false
};

async function browse(url){
const browser=await puppeteer.launch({
  headless:true,
  args:[
  '--no-sandbox',
  '--disable-setuid-sandbox',
  ]
});

try{
  const page=await browser.newPage();
  await page.setUserAgent('wh4t_a_cuT3_b0T_R1gHt');
  await page.setCookie(cookie);
  await page.goto(url);
  await browser.close();
}catch(error){
  await browser.close();
}finally{
  await browser.close();
}
  return true;
}
