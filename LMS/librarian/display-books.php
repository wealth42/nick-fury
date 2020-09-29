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
				</div>	
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="dbooks">
								<table id="dtBasicExample" class="table table-striped table-light text-center">
							<thead>
									<tr>
										<th>Books image</th>
										<th>Books name</th>
										<th>Author name</th>
										<th>Publication name</th>
										<th>Purchase date</th>
										<th>Books price</th>
										<th>Books quantity</th>
										<th>Books availability</th>
										<th>Delete book</th>
									</tr>
							</thead>
								
								<tbody>
								<?php
									$res = mysqli_query($link, "select * from add_book");
									while ($row = mysqli_fetch_array($res)) {
										echo "<tr>";
										echo "<td>"; ?><img src="<?php echo $row["books_image"]; ?> " height="100" width="100" alt=""> <?php echo "</td>";
										echo "<td>";
										echo $row["books_name"];
										echo "</td>";
										echo "<td>";
										echo $row["books_author_name"];
										echo "</td>";
										echo "<td>";
										echo $row["books_publication_name"];
										echo "</td>";
										echo "<td>";
										echo $row["books_purchase_date"];
										echo "</td>";
										echo "<td>";
										echo $row["books_price"];
										echo "</td>";
										echo "<td>";
										echo $row["books_quantity"];
										echo "</td>";
										echo "<td>";
										echo $row["books_availability"];
										echo "</td>";
										echo "<td>";
										?><a href="delete-book.php?id=<?php echo $row["id"]; ?> "><i class="fas fa-trash"></i></a><?php
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
	</body>
</html>
	<?php 
		include 'inc/footer.php';
	 ?>
   