import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';

import { RestService } from './rest.service';
import { AddEditNotificationDialogComponent } from './addEditNotificationDialog.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  displayedColumns: string[] = ['id', 'title', 'institution', 'actions'];
  dataSource = [];

  constructor(public rest: RestService, public dialog: MatDialog) {
  }

  ngOnInit() {
    this.getNotifications();
  }

  getNotifications() {
    this.rest.getNotifications().subscribe((data: any) => {
      console.log(data);
      this.dataSource = data;
    });
  }

  deleteNotification(id: any) {
    this.rest.deleteNotification(id).subscribe((data: any) => {
      this.getNotifications();
    });
  }

  addEditNotification(notification): void {
    const dialogRef = this.dialog.open(AddEditNotificationDialogComponent, {
      width: '450px',
      data: {notification}
    });

    dialogRef.afterClosed().subscribe(({isSaved}: any) => {
      if (isSaved) {
        this.getNotifications();
      }
    });
  }
}
