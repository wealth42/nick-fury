<?php 
	session_start();
    if (!isset($_SESSION["username"])) {
?>
		<script type="text/javascript">
			window.location="login.php";
		</script>
<?php
    }
    include 'inc/header.php';
    include 'inc/connection.php';
?>
<html>
	<head></head>
	<body>
		<!--dashboard area-->
		<div class="dashboard-content">
			<div class="dashboard-header">
				<div class="container">
					<div class="row">
				
						<div class="right">	
						<a href="dashboard.php">home</a>
						</div>
						
						<div class="right">
						<a href="profile.php">Profile</a>
						</div>
						
						<div class="right">
						<a href="logout.php">logout</a>
						</div>
					</div>
					<div class="issued-content">
						<div class="row">
							<div class="col-md-12">
								<div class="rbook-info status">
									<table id="dtBasicExample" class="table table-striped text-center">
										<thead>
												<tr>
													<th>Name</th>
													<th>Username</th>
													<th>User Type</th>
													<th>Email</th>
													<th>Status</th>
													<th>Action</th>
												</tr>
										</thead>
										<tbody>
											<?php
												$res= mysqli_query($link, "select * from std_registration ORDER BY id DESC");
												$res2= mysqli_query($link, "select * from t_registration ORDER BY id DESC");
												while ($row=mysqli_fetch_array($res)) {
													echo "<tr>";
													echo "<td>"; echo $row["name"]; echo "</td>";
													echo "<td>"; echo $row["username"]; echo "</td>";
													echo "<td>"; echo $row["utype"]; echo "</td>";
													echo "<td>"; echo $row["email"]; echo "</td>";
													echo "<td>"; echo $row["status"]; echo "</td>";
													echo "<td>";
													?>
														<ul>
															<li><a style="color: #000;" href="approve.php?id=<?php echo $row["id"]; ?>"><i class="fas fa-check"></i></a></li>
															<li><a href="notapprove.php?id=<?php echo $row["id"]; ?>"><i class="fas fa-allergies"></i></a></li>
														</ul>
													<?php
													echo "</td>";
													echo "</tr>";
												}
												while ($row=mysqli_fetch_array($res2)) {
													echo "<tr>";
													echo "<td>"; echo $row["name"]; echo "</td>";
													echo "<td>"; echo $row["username"]; echo "</td>";
													echo "<td>"; echo $row["utype"]; echo "</td>";
													echo "<td>"; echo $row["email"]; echo "</td>";
													echo "<td>"; echo $row["status"]; echo "</td>";
													echo "<td>";
													?>
														<ul>
															<li><a  style="color: #000;" href="approve.php?id=<?php echo $row["id"]; ?>"><i class="fas fa-check"></i></a></li>
															<li><a href="notapprove.php?id=<?php echo $row["id"]; ?>"><i class="fas fa-allergies"></i></a></li>
														</ul>
													<?php
													echo "</td>";
													echo "</tr>";
												}
											?>
										</tbody>
									</table>
								</div>
							</div>
						</div>
					</div>
				</div>					
			</div>
		</div>
	</body>
</html>
 <?php 
	include 'inc/footer.php';
 ?>