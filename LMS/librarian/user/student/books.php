<?php 
     session_start();
    if (!isset($_SESSION["student"])) {
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    $page = 'books';
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
					<div class="books">
						<form action="" method="post" name="form1">
							<table class="table ">
								<tr>
									<td>
										<input type="text" name="search" class="form-control" placeholder="Enter book name">
									</td>
									<td>
										<input type="submit" name="submit1" class="btn btn-info" value="Search Book">
									</td>
								</tr>
							</table>
						</form>
						<?php
							if (isset($_POST["submit1"])) {
								$i=0;
								$res = mysqli_query($link,"select * from add_book where books_name like('$_POST[search]%')"); 
								
								echo "<table class='table control-books'>";
								echo "<tr>";
								while ($row = mysqli_fetch_array($res)){
									$i=$i+1;
									echo "<td>";
									?> <a href="../<?php echo $row["books_file"]; ?>" target="_blank"><img src="../../<?php echo $row["books_image"]; ?> " alt=""></a> <?php 
									echo "</br>";
									echo "</br>";
									echo "<b>".$row["books_name"]; "</b>";
									echo "</br>";
									echo "<b>". 
									"Available: ".$row["books_availability"]; "</b>";
									echo "</td>";
									if ($i>=4) {
										echo "</tr>";
										echo "<tr>";
										$i=0;
									}
								}
								echo "</tr>";
								echo "</table>";
							}
							else{
								$i=0;
								$res = mysqli_query($link,"select * from add_book where books_availability>0");
								echo "<table id='dtBasicExample' class='table control-books'>";
								echo "<tr>";
								while ($row = mysqli_fetch_array($res)){
									$i=$i+1;
									echo "<td>";
									?> <a href="../../<?php echo $row["books_file"]; ?>" target="_blank"><img src="../../<?php echo $row["books_image"]; ?> " alt=""></a> <?php
									echo "</br>";
									echo "</br>";
									echo "<b>".$row["books_name"]; "</b>";
									echo "</br>";
									echo "<b>". 
									"Available: ".$row["books_availability"]; "</b>";
									echo "</td>";
	
									if ($i>=4) {
										echo "</tr>";
										echo "<tr>";
										$i=0;
									}
	
								}
								echo "</tr>";
								echo "</table>";
							}
						?>
					</div>
				</div>					
			</div>
		</div>
	</body>
</html>