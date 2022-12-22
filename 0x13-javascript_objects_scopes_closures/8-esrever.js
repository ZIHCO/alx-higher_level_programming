#!/usr/bin/node
/*
 * reverses a list
 */

exports.esrever = function (list) {
	reversedList = [];
	if (list) {
		for (let i = (list.length - 1); i >= 0; i--)
		{
			reversedList.push(list[i]);
		}
	}
	return reversedList;
}
