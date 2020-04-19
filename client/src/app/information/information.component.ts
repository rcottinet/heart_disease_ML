import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'information',
  templateUrl: './information.component.html',
  styleUrls: ['./information.component.css']
})
export class InformationComponent implements OnInit {

  gender = '';
  age: string = '';
  cigsByDay = '';
  bloodMeds = '';
  prevHyp = '';
  diabetes = '';
  totChol = '';
  glucose = '';
  sysBP = '';
  diaBP = '';

  result = '-1';

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  send(): void {
    // let data = {
    //   gender: this.gender,
    //   age: this.age,
    //   smoker: this.smoker,
    //   cigsByDay: this.cigsByDay,
    //   bloodMeds: this.bloodMeds,
    //   prevStroke: this.prevStroke,
    //   prevHyp: this.prevHyp,
    //   diabetes: this.diabetes,
    //   totChol: this.totChol,
    //   sysBP: this.sysBP,
    //   diaBP: this.diaBP,
    //   BMI: this.BMI,
    //   heartRate: this.heartRate,
    //   glucose: this.glucose
    // }

    // console.log(data);

    this.http.post<any>(
      'http://127.0.0.1:5000/results',
      {
        gender: this.gender,
        age: this.age,
        cigsByDay: this.cigsByDay,
        bloodMeds: this.bloodMeds,
        prevHyp: this.prevHyp,
        diabetes: this.diabetes,
        totChol: this.totChol,
        sysBP: this.sysBP,
        diaBP: this.diaBP,
        glucose: this.glucose
      }).subscribe(data => {
        console.log(data)
        this.result = data;
      })
  }

  cancel(): void {
    this.gender = '';
    this.age = '';
    this.cigsByDay = '';
    this.bloodMeds = '';
    this.prevHyp = '';
    this.diabetes = '';
    this.totChol = '';
    this.glucose = '';
    this.sysBP = '';
    this.diaBP = '';
    this.result = '-1';
  }

}
