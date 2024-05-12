function main (){
    const fechaA = new Date();
    const numeroDia = fechaA.getDay();
    const nombreDia = obtenerDia(numeroDia);
    console.log("Hoy es: " + nombreDia)
}

main();

function obtenerDia(numeroDia){
    const diaSemana = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];

    if (numeroDia >= 0 && numeroDia <= 6){
        return diaSemana[numeroDia];
    } else {
        const diaExtra = (numeroDia) % 7;
        return diaSemana[diaExtra];
    }
}       