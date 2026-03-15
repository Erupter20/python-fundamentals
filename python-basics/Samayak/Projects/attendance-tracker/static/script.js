function generateCalendar(){

const container=document.getElementById("calendar")

if(!container)return

const now=new Date()

const year=now.getFullYear()
const month=now.getMonth()

const firstDay=new Date(year,month,1).getDay()
const days=new Date(year,month+1,0).getDate()

const week=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

let html="<table><tr>"

for(let w of week){
html+="<th>"+w+"</th>"
}

html+="</tr><tr>"

for(let i=0;i<firstDay;i++){
html+="<td></td>"
}

for(let d=1;d<=days;d++){

html+="<td>"+d+"</td>"

if((d+firstDay)%7===0){
html+="</tr><tr>"
}

}

html+="</tr></table>"

container.innerHTML=html

}

generateCalendar()