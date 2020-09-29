    <?php 
      session_start();
        if (!isset($_SESSION["teacher"])) {
            ?>
                <script type="text/javascript">
                    window.location="login.php";
                </script>
            <?php
        }
        include 'inc/header.php';
        include 'inc/connection.php';
        mysqli_query($link,"update message set read1='y' where rusername='$_SESSION[teacher]'");

   ?>
   
	<!-- For Dropdown of MY PROFILE -->
	<script src="inc/js/jquery-2.2.4.min.js"></script>
	<script src="inc/js/custom.js"></script>
	
    <!--dashboard area-->
	<div class="dashboard-content">
		<div class="dashboard-header">
			<div class="container">
				<div class="row">
					<div class="right">	
					<a href="dashboard.php">Home</a>
					</div>
					
					<div class="right">
					<a href="profile.php">Profile</a>
					</div>
					
					<div class="right">
					<a href="logout.php">logout</a>
					</div>
                    <div class="col-md-12">
                        <table class="table table-bordered text-center table-striped">
							<h5><center>Message from Librarian </center></h5>
							<br>
                            <tr>
                                <th>Librarian name</th>
                                <th>Title</th>
                                <th>Message</th>
                                <th>Time</th>
                            </tr>
                            <?php 
                                 $res=mysqli_query($link,"select * from message where rusername='$_SESSION[teacher]' order by id desc");

                                  while ($row = mysqli_fetch_array($res)){
                                       $res1=mysqli_query($link,"select * from lib_registration where username='$row[susername]'");
                                       while ($row1 = mysqli_fetch_array($res1)){
                                           $name = $row1["name"];
                                       }

                                        echo "<tr>";
                                        echo "<td>"; echo $name; echo "</td>";
                                        echo "<td>"; echo $row["title"]; echo "</td>";
                                        echo "<td>"; echo $row["msg"]; echo "</td>";
                                        echo "<td>"; echo $row["time"]; echo "</td>";
                                        echo "</tr>";
                                  }
                             ?>
                        </table>
                    </div>
				</div>
			</div>					
		</div>
	</div>

    