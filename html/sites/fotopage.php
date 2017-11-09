<?php
$Path = getcwd();
$FOLDER = dir("static/images/gallery");
$LOOPINDEX = 0;
?>
{% extends "layout.html" %}
{% block head %}
<!--script src="static/js/jquery/jquery.js"></script -->
<script src="static/js/blueimp/blueimp-gallery.js"></script>
<!-- script src="/ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script -->
<script src="static/js/blueimp/jquery.blueimp-gallery.js"></script>
<link rel="stylesheet" href="static/css/blueimp/blueimp-gallery.min.css">
{% endblock %}
{% block body %}
{% include "util/nav_bar.html" %}
<div class="row">
    <div class="col-md-1">
    </div>
    <div class="col-md-9">
        <div class="well">
<?php while ($ALBEN = $FOLDER->read()){
        	if ($ALBEN === "." || $ALBEN === "..") {
        		continue;
        	}
        	$VALUE = str_replace("_", " ", $ALBEN);
            if ($LOOPINDEX % 3 === 0)
            	echo "\t\t<div class=\"row\" style=\"margin:10px\">\n";
            ?>			<div class="col-md-4">
                    <a href="/album.php?name=<?php echo $ALBEN; ?>"><img src="static/images/gallery/<?php echo $ALBEN; ?>/<?php
                    $SHOW_PIC = dir("static/images/gallery/" . $ALBEN );
                    while($PICTURE= $SHOW_PIC->read()){
                    	if ($ALBEN === "." || $ALBEN === "..") {
                    		continue;
                    	}
                    	if (preg_match_all("/\.(jpe?g|GIF|png)/i", $PICTURE) > 0){
                    		echo $PICTURE;//."\">";
                    		break;
        				}
                    }?>" class="img-responsive"></a>
        			<h4><?php echo $VALUE;?></h4>
            </div>
<?php

		$LOOPINDEX++;
		if($LOOPINDEX % 3 === 0){
			echo "\t\t</div>\n";
		}
        }
        if($LOOPINDEX % 3 !== 0){
        	echo "\t\t</div>\n";
        }
        ?>
        </div>
<?php $FOLDER->close();?>
    </div>

    <div class="col-md-2"></div>
</div>
<script type="application/javascript">
   var elements = document.getElementsByClassName('img-item');
   console.log(elements);
   /*for( int i = 0; i< elements.length; i++){
        ;
   }*/

};

</script>
{% endblock %}
