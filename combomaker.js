var moveList = {
  "5P" : "NmlAtk5A",
  "6P" : "NmlAtk6A",
  "2P" : "NmlAtk2A",
  "5K" : "NmlAtk5B",
  "2K" : "NmlAtk2B",
  "6K" : "NmlAtk6B",
  "c.S" : "NmlAtk5CNear",
  "f.S" : "NmlAtk5CFar",
  "2S" : "NmlAtk2C",
  "5H" : "NmlAtk5D",
  "2H" : "NmlAtk2D",
  "6H" : "NmlAtk6D",
  "5D" : "NmlAtk5E",
  "2D" : "NmlAtk2E",
  "5D8" : "Homing Jump",
  "5D6" : "Homing Dash",
  "j.A" : "NmlAtkAir5A",
  "j.K" : "NmlAtkAir5B",
  "j.S" : "NmlAtkAir5C",
  "j.H" : "NmlAtkAir5D",
  "j.D" : "NmlAtkAir5E",
  "46P" : "TuikaA",
  "46PP" : "
  "236SSH" : ["Bakushuu", "HyappoShinshou", "HaseiSenriShinshou"]
};

var combo = "5P > 2P > 236SSH";
var comboList = combo.toUpperCase().split(" > ");
var combo = [];
for (var move in comboList) {
  combo = combo.concat(moveList[comboList[move]]);
}

console.log(combo);