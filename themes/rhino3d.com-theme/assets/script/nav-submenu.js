// WWW-3627: navbar submenus (partials/site-navigation.html).
//
// CSS alone can open these on :hover, but that closes the instant the pointer
// leaves the group's own box — a curved or fast path toward an item, or the
// navbar shifting under the pointer when the page scrolls a little, drops the
// menu mid-travel. So the pointer opens it here and closing waits out a short
// grace period, which a return to the group cancels. The :hover rule stays in
// the stylesheet as the no-JS fallback.
//
// Touch gets a tap toggle on parents that are not links; a parent with a url
// still navigates on tap.
(function () {
	"use strict";

	var CLOSE_DELAY = 400;
	var groups = [].slice.call(document.querySelectorAll(".menu-item-group"));
	if (!groups.length) return;

	var timers = new WeakMap();

	function close(group) {
		group.classList.remove("open");
	}

	function open(group) {
		clearTimeout(timers.get(group));
		groups.forEach(function (other) {
			if (other !== group) close(other);
		});
		group.classList.add("open");
	}

	function scheduleClose(group) {
		clearTimeout(timers.get(group));
		timers.set(group, setTimeout(function () {
			close(group);
		}, CLOSE_DELAY));
	}

	groups.forEach(function (group) {
		group.addEventListener("pointerenter", function () {
			open(group);
		});

		group.addEventListener("pointerleave", function () {
			scheduleClose(group);
		});

		var parent = group.querySelector(".menu-item-parent");
		if (parent && parent.tagName !== "A") {
			parent.addEventListener("click", function () {
				if (group.classList.contains("open")) close(group);
				else open(group);
			});
		}
	});

	document.addEventListener("keydown", function (event) {
		if (event.key === "Escape") groups.forEach(close);
	});

	document.addEventListener("click", function (event) {
		groups.forEach(function (group) {
			if (!group.contains(event.target)) close(group);
		});
	});
})();
