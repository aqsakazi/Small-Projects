function kgtop(val1) {
    var val1 = val1 * 2.2046;
    var n = val1.toFixed(0);
    document.getElementById("outputPounds").innerHTML = n;
}

function ptokg(val2) {
    var val2 = val2 / 2.2046;
    var m = val2.toFixed(0);
    document.getElementById("outputKilograms").innerHTML = m;
}