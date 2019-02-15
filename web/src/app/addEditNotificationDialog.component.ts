import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material';
import { RestService } from './rest.service';

@Component({
  selector: 'app-dialog-overview-example-dialog',
  templateUrl: 'addEditNotificationDialog.html',
})
export class AddEditNotificationDialogComponent implements OnInit {

  institutions: any = [];
  id: any;
  title: any;
  institution: any;

  constructor(
    public rest: RestService,
    public dialogRef: MatDialogRef<AddEditNotificationDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any) {
    if (data && data.notification) {
      this.id = data.notification.id;
      this.title = data.notification.title;
      this.institution = data.notification.institution.id;
    }
  }

  ngOnInit() {
    this.getInstitutions();
  }

  getInstitutions(): void {
    this.rest.getInstitutions().subscribe((data: any) => {
      console.log(data);
      this.institutions = data;
    });
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  onYesClick(): void {
    console.log(this.institution);
    let observer = this.rest.updateNotification(this.id, {title: this.title, institution: this.institution});
    if (!this.id) {
      observer = this.rest.addNotification({title: this.title, institution: this.institution});
    }

    observer.subscribe((data: any) => {
      console.log(data);
      this.dialogRef.close({isSaved: true});
    });
  }

}
