

window.onload = function () {
    hit_data.map((hit) => {
        hit.pitchside = (hit.pitchside=='R')? 'Right' : 'Left'
    })
    var data = []

    var chart=new CanvasJS.Chart("chartContainer", {
        animationEnabled: false,
        backgroundColor: "transparent",
        zoomEnabled: false,
        width: 400,
        height: 400,
        title: {
            text: "Hits"
        },
        axisX: {
            title: "distance (in ft.)",
            minimum: -200,
            maximum: 200
        },
        axisY: {
            title: "distance (in ft.)",
            minimum: 0,
            maximum: 420
        },
        data: [{
            type: "scatter",
            toolTipContent: "<b>Date: </b>{date}</br><b>Pitcher: </b>{pitcher} who pitches with his {pitchside} hand </br><b>LaunchSpeed: </b>{launchspeed}mph</br><b>Result:</b>{result_type}",
            dataPoints: data
        }]
    });


    const updatechart = (newdata) => {
    

        data.splice(0,data.length)
        data.push(...newdata)
        chart.render();
    }
    
    const form = document.getElementById('filter');
    form.addEventListener('change', function(e) {
        var filter = document.getElementById(e.target.value)
        
        var filterForms = document.getElementsByClassName("chartFilter")
    
        for (var i=0, len=filterForms.length|0; i<len; i=i+1|0) {
            filterForms[i].hidden=true
        }
        filter.hidden=false
        updatechart([])
    });

    const resultForm = document.getElementById('result')
    resultForm.addEventListener('change', function(e) {
        if (e.target.value =='all'){
            data.splice(0,data.length)
            data.push(...hit_data)
            chart.render()
        }else{
            data.splice(0,data.length)
            data.push(...hit_data)
            const newdata = data.filter((datum)=> {
                return datum.result_type === e.target.value
            })
            data.splice(0,data.length)
            data.push(...newdata)
            chart.render()
        }
    })

    const pitchTypeForm = document.getElementById('pitchType')
    pitchTypeForm.addEventListener('change', function(e) {
        if (e.target.value =='all'){
            data.splice(0,data.length)
            data.push(...hit_data)
            chart.render()
        }else{
        data.splice(0,data.length)
        data.push(...hit_data)
        const newdata = data.filter((datum)=> {
            return datum.pitch_type === e.target.value
        })
        data.splice(0,data.length)
        data.push(...newdata)
        chart.render()
    }
    })


    updatechart(hit_data)

}



