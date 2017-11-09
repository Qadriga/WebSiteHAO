
<?php
class UpcommingDate{
	private $date;
	private $link;
	private $name;
	
	public function __construct($date ,$link ,$Name){
		$this->link = $link;
		$this->date = $date;
		$this->name = $Name;
	}
	public function getDate(): DateTime{
		if(is_null($this->date)){
			return new DateTime();
		}
			return $this->date;
	}
	public function getLink():string {
		if(is_null($this->link)){
			return "";
		}
		return $this->link;
	}
	public function getName():string {
		if(is_null($this->name)){
			return "";
		}
		return $this->name;
	}
}