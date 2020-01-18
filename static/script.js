function myFunction() {
  document.getElementById("myNumber").placeholder = "Amount";
}

document.getElementById("number").onblur =function (){    
    this.value = parseFloat(this.value.replace(/,/g, ""))
                    .toFixed(2)
                    .toString()
                    .replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    
 document.getElementById("display").value = this.value.replace(/,/g, "")
}

const countriesList = document.getElementById("countries");

    function newCountrySelection(event) {
      displayCountryInfo(event.target.value);
}

  fetch("https://restcountries.eu/rest/v2/all")
  .then(res => res.json())
  .then(data => initialize(data))
  .catch(err => console.log("Error:", err));

function initialize(countriesData) {
  countries = countriesData;
  let options = "";

  countries.forEach(country => options+=`<option value="${country.name}">${country.name}</option>`);

  countriesList.innerHTML = options;

  countriesList.selectedIndex = Math.floor(Math.random()*countriesList.length);

}

    function compareDates() {

        var Startdate= new ('statedate');
        var Enddate= new Date ('enddate');
  
        if(Startdate>Enddate)
        {
        alert= ("start date is greater than end date.");
        }
        else if(Enddate>Startdate);
        {
        alert= ("End date is greater than start date.");
     
        }       
    }
    
    compareDates();

