<?php
session_start();
$conn= new mysqli('localhost','root','','hospitalmanagement');
?>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="main.css">
	<title>Appointment History </title>
</head>
<body>
	<?php
	if(isset($_SESSION["username"]))
	{
		?>
		<div class="container">
			<h2> Appointment Records </h2>
			<br>
			<hr>    
			<br>
			<div class="table100 ver4 ">
				<table data-vertable="ver4">
					<thead>
						<tr class="row100 head">
							<th class="column100 column1" data-column="column1">doctor</th>
							<th class="column100 column2" data-column="column2">date </th>
							<th class="column100 column3" data-column="column3">timeslot</th>	
							<th class="column100 column4" data-column="column4">contact</th>
							<th class="column100 column5" data-column="column5">address</th>
							<th class="column100 column6" data-column="column6">disease</th>
							<th class="column100 column7" data-column="column7">view</th>
						</tr>
					</thead>
					<?php
					$sql = "SELECT * FROM appointment where patient='".$_SESSION["email"]."'";
					$result=$conn->query($sql);
					if($result->num_rows > 0){
						while($rows= $result->fetch_assoc()){
							?>
							<tbody>
								<tr class="row100">
									<td class="column100 column1" data-column="column1"><?php echo $rows["doctor"]; ?></td>
									<td class="column100 column2" data-column="column2"><?php echo $rows["date"]; ?></td>
									<td class="column100 column3" data-column="column3"><?php echo $rows["timeslot"]; ?></td>
									<td class="column100 column4" data-column="column4"><?php echo $rows["contact"]; ?></td>
									<td class="column100 column5" data-column="column5"><?php echo $rows["address"]; ?></td>
									<td class="column100 column6" data-column="column6"><?php echo $rows["disease"]; ?></td>
									<td class="column100 column7" data-column="column7"><a href="view.php?id=<?php echo $rows["id"];?>" > View </a></td>
								</tr>
							</tbody>
							<?php 
						}
					}
					?>
				</table>
			</div>
		</div>
		<?php 
	}
	else{
		echo "<script>location.href='patientlogin.php'</script>";
	}
	?>
</body>
</html>	