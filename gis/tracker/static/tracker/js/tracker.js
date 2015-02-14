;(function() {
    //alert("HI");
    //var obj = call_counter();

    //var person1 = new createperson(001, {x: 250, y:250},{x:200,y:400},{x:0.5,y:0.5});
    //var person2 = new createperson(002, {x: 150, y:350},{x:0,y:100},{x:0.5,y:0.5});
    //var person3 = new createperson(003, {x: 50, y:500},{x:320,y:400},{x:0.5,y:0.5});
    //var person4 = new createperson(004, {x: 60, y:150},{x:110,y:410},{x:0.5,y:0.5});
    //var person5 = new createperson(005, {x: 80, y:350},{x:310,y:120},{x:0.5,y:0.5});
    //var person6 = new createperson(006, {x: 100, y:250},{x:290,y:149},{x:0.5,y:0.5});

    
    //var person1 = new createperson(data[0].person_id, {x: 0, y: 0}, {data[0].x,data[0].y}, {x:0,y:0});
    var OOIList = [];

    function initializeperson(){
        var obj = call_counter();
        var OList = [];
        var temparray = [];

        //split data into an array for each person
        for (i=0; i<obj.length-1; i++){

            if (obj[i].person_id == obj[i+1].person_id){
                temparray.push(obj[i]);
            }

            else if (obj[i].person_id != obj[i+1].person_id){
                temparray.push(obj[i]);
                OList.push(temparray);
                temparray = [];
            }

            if (i+1==obj.length-1){
                temparray.push(obj[i+1]);
                OList.push(temparray);
                temparray=[];
            }
        }

        //Initialize each OOI, and store a vector of position data with that person
        var temparray2 = [];

        for (i=0; i<OList.length; i++){
            temparray2=[];
            OOIList[i] = new createperson(OList[i][0].person_id, {x: OList[i][0].x,y: OList[i][0].y}, {x: OList[i][1].x,y: OList[i][1].y},{x: 0,y: 0},{x:0,y:0});

            for (j=0; j<OList[i].length; j++){
                temparray2.push({x: OList[i][j].x, y: OList[i][j].y});
            }
            temparray2.shift();    //shift twice to get to the new position data
            temparray2.shift();
            OOIList[i].vector = temparray2; 
        }

        return OOIList;
    }

    function createperson(ID, position, target, step, vector) {
        this.ID = ID;
        this.position = position;
        this.target = target;
        this.step = step;
        this.vector = vector;
    }

    function updatetarget(OOIList){
        var temparray=[];
        for (i=0; i<OOIList.length; i++){
            if(typeof OOIList[i].vector != "undefined" && OOIList[i].vector != null && OOIList[i].vector.length > 0){
                OOIList[i].position = OOIList[i].target;
                OOIList[i].target = OOIList[i].vector[0];
                temparray = OOIList[i].vector;
                temparray.shift();
                OOIList[i].vector = temparray;
            }
        }
    }

    function tick() {
        draw(OOIList);
    };

    function call_counter() {
        var result = null;
        var scriptURL = 'tracks/';
        $.ajax({
            url: scriptURL,
            type: 'get',
            async: false,
            success: function(data){
                result = data;
            }
        });
        return result;
    }

    function init() {
        initializeperson();

        canvas = document.getElementById('canvas');
        canvobj = canvas.getContext('2d');
        canvobj.translate(0,canvas.height);
        canvobj.scale(1,-1);

        setInterval(tick, 1000/60);
    }

    function draw(OOIList){

        var scale = 20;
        canvobj.clearRect(0, 0, canvas.width, canvas.height);

          // If They are not within a specified distance color orange
        for (i=0; i<OOIList.length; i++){

            canvobj.fillStyle = "rgb(243,119,11)";
            canvobj.beginPath();
            canvobj.arc(OOIList[i].position.x*scale,OOIList[i].position.y*scale,10,0,Math.PI*2);
            canvobj.fill();
            canvobj.closePath();

            // If They are within a specified distance color red
            for (j=0; j<OOIList.length; j++){
                if ((i != j) && (Math.abs(OOIList[i].position.x*scale - OOIList[j].position.x*scale) < 30) && (Math.abs(OOIList[i].position.y*scale - OOIList[j].position.y*scale) < 30) ){

                    canvobj.fillStyle = "rgb(226,8,8)";
                    canvobj.beginPath();
                    canvobj.arc(OOIList[i].position.x*scale,OOIList[i].position.y*scale,10,0,Math.PI*2);
                    canvobj.fill();
                    canvobj.closePath();

                    canvobj.fillStyle = "rgb(226,8,8)";
                    canvobj.beginPath();
                    canvobj.arc(OOIList[j].position.x*scale,OOIList[j].position.y*scale,10,0,Math.PI*2);
                    canvobj.fill();
                    canvobj.closePath();

                }
            }

            OOIList[i].step = step(OOIList[i]);

            //console.log(OOIList[0].position);


            if (Math.floor(OOIList[i].position.x) != OOIList[i].target.x){
            OOIList[i].position.x += OOIList[i].step.x;
            }
            if (Math.floor(OOIList[i].position.y) != OOIList[i].target.y){
            OOIList[i].position.y += OOIList[i].step.y;
            }
            if ((Math.floor(OOIList[i].position.y) == OOIList[i].target.y) && (Math.floor(OOIList[i].position.x) == OOIList[i].target.x)){
                updatetarget(OOIList);
                //console.log(OOIList[0].position);
            }

        }

        // Proximity Check (Change Color) DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for (i=0; i<OOIList.length; i++){
            for (j=0; j<OOIList.length; j++){
                if ((i != j) && (Math.abs(OOIList[i].position.x - OOIList[j].position.x) < 20)){

                }
            }
        }
    }

    function step(person) {
        var xmov = person.target.x - person.position.x;
        var ymov = person.target.y - person.position.y;
        var length = Math.sqrt(xmov * xmov + ymov * ymov);

        return {x: 0.1*(xmov / length), y: 0.1*(ymov / length)};
    }


    window.onload = function() {
        console.log("HI");
        init();
    };

})();
