import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

const endpoint = 'http://localhost:8000/api/v1.0/';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) {
  }

  private extractData(res: Response) {
    const body = res;
    return body || {};
  }

  getInstitutions(): Observable<any> {
    return this.http.get(endpoint + 'institutions').pipe(
      map(this.extractData));
  }

  getNotifications(): Observable<any> {
    return this.http.get(endpoint + 'notifications').pipe(
      map(this.extractData));
  }

  getNotification(id): Observable<any> {
    return this.http.get(endpoint + 'notifications/' + id).pipe(
      map(this.extractData));
  }

  addNotification(notification): Observable<any> {
    console.log(notification);
    return this.http.post<any>(endpoint + 'notifications/', JSON.stringify(notification), httpOptions).pipe(
      tap((notification) => console.log(`added notification w/ id=${notification.id}`)),
      catchError(this.handleError<any>('addNotification'))
    );
  }

  updateNotification(id, notification): Observable<any> {
    console.log(notification)
    return this.http.put(endpoint + 'notifications/' + id + '/', JSON.stringify(notification), httpOptions).pipe(
      tap(_ => console.log(`updated notification id=${id}`)),
      catchError(this.handleError<any>('updateNotification'))
    );
  }

  deleteNotification(id): Observable<any> {
    return this.http.delete<any>(endpoint + 'notifications/' + id, httpOptions).pipe(
      tap(_ => console.log(`deleted notification id=${id}`)),
      catchError(this.handleError<any>('deleteNotification'))
    );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.error(error);
      console.log(`${operation} failed: ${error.message}`);

      return of(result as T);
    };
  }
}
