package com.example.avinash.communitymessage;

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.telephony.SmsManager;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

     Button button;

    EditText editText4, editText3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (ContextCompat.checkSelfPermission(MainActivity.this,
                Manifest.permission.SEND_SMS) != PackageManager.PERMISSION_GRANTED) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this,
                    Manifest.permission.SEND_SMS)) {
                ActivityCompat.requestPermissions(MainActivity.this,
                        new String[]{Manifest.permission.SEND_SMS}, 1);
            } else {
                ActivityCompat.requestPermissions(MainActivity.this,
                        new String[]{Manifest.permission.SEND_SMS}, 1);
            }
        } else {

            // do nothing

        }

        button = (Button) findViewById(R.id.button);

        editText4 = (EditText) findViewById(R.id.editText4);
        editText3 = (EditText) findViewById(R.id.editText3);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String number = editText4.getText().toString();
                String sms = editText3.getText().toString();

                try {
                    SmsManager smsManager = SmsManager.getDefault();
                    smsManager.sendTextMessage(number, null, sms, null, null);
                    Toast.makeText(MainActivity.this, "Sent!", Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    Toast.makeText(MainActivity.this, "Failed!", Toast.LENGTH_SHORT).show();


                }
            }
        });
    }


                 @Override

     public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults){
          switch (requestCode) {
              case 1: {
                 if(grantResults.length>0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                     if (ContextCompat.checkSelfPermission(MainActivity.this,
                             Manifest.permission.SEND_SMS) == PackageManager.PERMISSION_GRANTED) {
                         Toast.makeText(this, "Permission granted!", Toast.LENGTH_SHORT).show();
                     }
                 }else {
                     Toast.makeText(this, "No permission granted!", Toast.LENGTH_SHORT).show();
                 }
                 return;


                     }}
              }
          }