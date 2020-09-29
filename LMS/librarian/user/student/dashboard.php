<?php 
     session_start();
    if(!isset($_SESSION["student"])) {
		$id=$_GET["id"];
        ?>
            <script type="text/javascript">
                window.location="login.php";
            </script>
        <?php
    }
    $page ='home';
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
				
				
					<div class="row counterup">
					
						<div class="col-md-3 col-sm-3 col-xs-12 control">
							<div class="box">
								<div class="icon">
									<i class="fa fa-rocket"></i>
								</div>
								<div class="text">
									<h3><span class="counter">
										<?php
											$res2= mysqli_query($link, "select * from issue_book where username='".$_SESSION['student']."'");
											$count2 = mysqli_num_rows($res2);
											echo $count2;
										?>
										</span></h3>
									<h4><a href="my-issued-books.php">Issued books</a></h4>
								</div>
							</div>
						</div>
						
						<div class="col-md-3 col-sm-3 col-xs-12 control">
							<div class="box box2">
								<div class="icon">
									<i class="fas fa-book"></i>
								</div>
								<div class="text">
									<h4 class="mt-20"><a href="books.php">Manage Book</a></h4>
								</div>
							</div>
						</div>
						
						<div class="col-md-3 col-sm-3 col-xs-12 control">
							<div class="box box3">
								<div class="icon">
									<i class="fas fa-user"></i>
								</div>
								<div class="text">
									<h4 class="mt-20"><a href="profile.php">Manage Profile</a></h4>
								</div>
							</div>
						</div>
						
						<div class="col-md-3 col-sm-3 col-xs-12 control">
							<div class="box box4">
								<div class="icon">
									<i class="fas fa-book"></i>
								</div>
								<div class="text">
									<h4 class="mt-20"><a href="request-book.php">Request Books</a></h4>
								</div>
							</div>
						</div>
						
					</div>
				</div>
			</div>
		</div>
	</body>
</html>