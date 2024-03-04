document.ready(function () {
	const myAmenities = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
			myAmenities[this.dataset.name] = this.dataset.id;
		} else {
			delete myAmenities[this.dataset.name];
		}
		$(".amenities h4").text(Object.keys(myAmenities).sort().join(", "));
	});
});
