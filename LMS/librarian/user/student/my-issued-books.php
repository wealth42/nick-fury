<?php 
     session_start();
    if (!isset($_SESSION["student"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    $page = 'ibook';
    include 'inc/header.php';
    include 'inc/connection.php';
 ?>
 <html>
	<head>
    <!-- Important Script Files -->
	<script src="inc/js/jquery-2.2.4.min.js"></script>
	<script src="inc/js/custom.js"></script>
	<!-- dashboard area-->
	</head>
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
				</div>
				
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="st-issuedBook">
								<table id="dtBasicExample" class="table table-striped text-center">
									<thead>
									<tr>
											<th>Reg No</th>
											<th>Username</th>
											<th>Books Name</th>
											<th>Books Issue Date</th>
											<th>Books Return Date</th>
									</tr>
									</thead>
									<tbody>
									<?php 
										$res= mysqli_query($link, "select * from issue_book where username='".$_SESSION['student']."' ORDER BY id DESC");
										while ($row=mysqli_fetch_array($res)) {
											echo "<tr>";
											echo "<td>"; echo $row["regno"]; echo "</td>";
											echo "<td>"; echo $row["username"]; echo "</td>";
											echo "<td>"; echo $row["booksname"]; echo "</td>";
											echo "<td>"; echo $row["booksissuedate"]; echo "</td>";
											echo "<td>"; echo $row["booksreturndate"]; echo "</td>";
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
	</body>
</html>