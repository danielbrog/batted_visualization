const playerID= window.location.pathname.split("/").pop()

fetch('https://statsapi.mlb.com/api/v1/people/'+ playerID + '?hydrate=stats').then((res)=>{
    return res.json()
}).then((res)=>{
    document.getElementById('age').innerHTML=document.getElementById('age').innerHTML + ' ' + res.people[0].currentAge
    document.getElementById('height').innerHTML=document.getElementById('height').innerHTML + ' ' + res.people[0].height
    const pitchexists = document.getElementById('pitchHand')
    const batExists = document.getElementById('batHand')
    if(pitchexists){
        document.getElementById('pitchHand').innerHTML=document.getElementById('pitchHand').innerHTML + ' ' + res.people[0].pitchHand.description
    } else if(batExists){
        document.getElementById('batHand').innerHTML=document.getElementById('batHand').innerHTML + ' ' + res.people[0].batSide.description
    }
})