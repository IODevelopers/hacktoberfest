//: Playground - noun: a place where people can play

import Foundation

let now = Date()

let yesterday = Calendar.current.date(byAdding: .day, value: -1, to: now)!

Calendar.current.isDateInToday(now)
Calendar.current.isDateInToday(yesterday)
