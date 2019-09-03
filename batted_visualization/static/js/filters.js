import newchart from '/static/js/scatterplot.js'

var form = document.getElementById('filter');
form.addEventListener('change', function(e) {
    var filter = document.getElementById(e.target.value)
    
    var filterForms = document.getElementsByClassName("chartFilter")

    for (var i=0, len=filterForms.length|0; i<len; i=i+1|0) {
        filterForms[i].hidden=true
    }
    filter.hidden=false
    newchart([])
});