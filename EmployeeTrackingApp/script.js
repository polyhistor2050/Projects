class Employee {
    constructor(firstname, lastname, years) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.years = years;
    }
   }

   const worker1 = new Employee("Carter", "Hermione", 5);
   const worker2 = new Employee("Bob", "Crane", 3);
   const worker3 = new Employee("Boozer", "ruscov", 6);
   let workers = [worker1, worker2, worker3];

   Employee.prototype.details = function () {
    return this.firstname + " " + this.lastname + " has worked here for " + this.years + " years";
   }

   workers.forEach((worker) => {
    console.log(worker.details())
   });