import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Patient {
  gender: string;
  age: string;
  cigsByDay: string;
  bloodMeds: string;
  prevHyp: string;
  diabetes: string;
  totChol: string;
  glucose: string;
  sysBP: string;
  diaBP: string;
  result?: string;
  proba?: string;
  date?: Number;
}

@Component({
  selector: 'information',
  templateUrl: './information.component.html',
  styleUrls: ['./information.component.css']
})
export class InformationComponent implements OnInit {

  histPatient: Array<Patient> = []

  patient: Patient = {
    gender: '',
    age: '',
    cigsByDay: '',
    bloodMeds: '',
    prevHyp: '',
    diabetes: '',
    totChol: '',
    glucose: '',
    sysBP: '',
    diaBP: '',
    result: '',
    proba: ''
  }

  result = '-1';
  proba = '';

  patient_positif: Patient;
  patient_negatif: Patient;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {

    this.patient_positif = { gender: '1', age: '50', cigsByDay: '1', bloodMeds: '0', prevHyp: '1', diabetes: '0', totChol: '313', sysBP: '92', diaBP: '86', glucose: '179', result: '1', proba: '51' }

    this.patient_negatif = { gender: '0', age: '46', cigsByDay: '0', bloodMeds: '0', prevHyp: '0', diabetes: '0', totChol: '250', sysBP: '81', diaBP: '76', glucose: '121', result: '0', proba: '92' }

  }

  send(): void {

    this.http.post<any>(
      'http://127.0.0.1:5000/results',
      {
        gender: this.patient.gender,
        age: this.patient.age,
        cigsByDay: this.patient.cigsByDay,
        bloodMeds: this.patient.bloodMeds,
        prevHyp: this.patient.prevHyp,
        diabetes: this.patient.diabetes,
        totChol: this.patient.totChol,
        sysBP: this.patient.sysBP,
        diaBP: this.patient.diaBP,
        glucose: this.patient.glucose
      }).subscribe(data => {
        console.log(data)

        this.result = data.result;
        if (this.result == '0') {
          this.proba = String(Math.round(data.proba * 100));
        } else {
          this.proba = String(100 - Math.round(data.proba * 100));
        }
        this.patient.result = this.result;
        this.patient.proba = this.proba;
        this.patient.date = Date.now();
        this.histPatient.push(this.patient)
      })
  }

  cancel(): void {
    this.patient.gender = '';
    this.patient.age = '';
    this.patient.cigsByDay = '';
    this.patient.bloodMeds = '';
    this.patient.prevHyp = '';
    this.patient.diabetes = '';
    this.patient.totChol = '';
    this.patient.glucose = '';
    this.patient.sysBP = '';
    this.patient.diaBP = '';
    this.patient.result = '-1';
  }

  selectPatient(patient: Patient): void {
    this.patient = Object.assign(patient);
  }
}
