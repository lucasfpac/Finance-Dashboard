const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table")
const pagination = document.querySelector(".pagination-container")
const tableBody = document.querySelector(".table-body")
tableOutput.style.display = "none";

searchField.addEventListener('keyup', (e)=>{
    const searchValue = e.target.value;


    if(searchValue.trim().length > 0){
        pagination.style.display = "none";
        tableBody.innerHTML = "";
        fetch("/search-expenses", {
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);

                appTable.style.display = "none";
                tableOutput.style.display = "block";
                
            if (data.length === 0){
                
                tableOutput.innerHTML = "No results found!"
                

            } else{
                    
                data.forEach((item)=>{
                    tableBody.innerHTML+=`
                    <tr>
                        <td>${item.amount}.0</td>
                        <td>${item.description}</td>
                        <td>${item.category}</td>
                        <td>${item.date}</td>
                    </tr>
                    `
                });
              
            }
            });
    }else{
        appTable.style.display = "block";
        tableOutput.style.display = "none";
        pagination.style.display = "block";

    }
})