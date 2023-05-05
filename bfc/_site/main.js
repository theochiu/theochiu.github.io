function calcBodyFat() {
	var leanmass = document.getElementById("leanmass").value;
	var totalmass = document.getElementById("totalmass").value;
	leanmass = Number(leanmass);
	totalmass = Number(totalmass);

	if (totalmass < leanmass) {
		document.getElementById("results_div").innerHTML = "Your total mass is less than your lean mass, this is impossible";
		return
	}


	var currentbodyfatpercentage = (totalmass - leanmass) / totalmass * 100;
	currentbodyfatpercentage = Math.round(currentbodyfatpercentage * 1000) / 1000


	console.log(currentbodyfatpercentage);

	// create a table of various body fat percentages
	// and corresponding weight

	var table = "<table>\
	<tr>\
		<th>Bodyfat (%)</th>\
		<th>Total weight</th>\
	</tr>";

	if (currentbodyfatpercentage < 5) {
		table += "<b><tr> \
			<td>" + currentbodyfatpercentage + " </td> \
			<td>" + totalmass + "</td> \
			</tr></b>"
	}

	for (let i=5; i<=25.5; i+=1.5) {
		var weight = leanmass + leanmass / ((100 / i) - 1)
		weight = Math.round(weight * 1000) / 1000

		if (weight == totalmass) {
			table += "<b><tr> \
				<td>" + i + " </td> \
				<td>" + weight + "</td> \
				</tr></b>"
		}
		else {
			table += "<tr> \
				<td>" + i + " </td> \
				<td>" + weight + "</td> \
				</tr>"
		}
		if (currentbodyfatpercentage > i && currentbodyfatpercentage < i + 1.5) {
			table += "<tr> \
				<td style=\"font-weight:bold\">" + currentbodyfatpercentage + " </td> \
				<td style=\"font-weight:bold\">" + totalmass + "</td> \
				</tr>"			
		}
	}

	if (currentbodyfatpercentage > 25.5) {
		table += "<b><tr> \
			<td>" + currentbodyfatpercentage + " </td> \
			<td>" + totalmass + "</td> \
			</tr></b>"
	}
	table += "</table>"

	if (currentbodyfatpercentage < 5) {
		table += "Your body fat is dangerously low!"
	}

	else if (currentbodyfatpercentage > 20) {
		table += "Your body fat is dangerously high!"
	}


		
	document.getElementById("results_div").innerHTML = table;

}