using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    public float speed;
    public float power;

    // Update is called once per frame
    void Update()
    {
        if (!Input.GetKey(KeyCode.Space))
        {
            if (Input.GetKey(KeyCode.W))
            {
                transform.Translate(Vector3.forward * Time.deltaTime * speed);
            }
            if (Input.GetKey(KeyCode.W) && Input.GetKey(KeyCode.LeftShift))
            {
                transform.Translate(3 * Vector3.forward * Time.deltaTime * speed);
            }
            if (Input.GetKey(KeyCode.S))
            {
                transform.Translate(-1 * Vector3.forward * Time.deltaTime * speed);
            }
            if (Input.GetKey(KeyCode.S) && Input.GetKey(KeyCode.LeftShift))
            {
                transform.Translate(-2 * Vector3.forward * Time.deltaTime * speed);
            }
            if (Input.GetKey(KeyCode.D))
            {
                transform.Translate(Vector3.right * Time.deltaTime * speed);
            }
            else if (Input.GetKey(KeyCode.A))
            {
                transform.Translate(-1 * Vector3.right * Time.deltaTime * speed);
            }
        }


    }
}
