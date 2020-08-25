using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DogAnimation : MonoBehaviour
{
    Animator animator;

    void Start()
    {
        animator = GetComponent<Animator>();
    }
    void Update()
    {
        if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.D))
        {
            animator.SetBool("isWalking", true);
        }
        if ((Input.GetKey(KeyCode.W)|| Input.GetKey(KeyCode.S)) && Input.GetKey(KeyCode.LeftShift))
        {
            animator.SetBool("isRunning", true);
            animator.SetBool("isWalking", false);
        }

        if (Input.GetKeyUp(KeyCode.W) || Input.GetKeyUp(KeyCode.S) || Input.GetKeyUp(KeyCode.A) || Input.GetKeyUp(KeyCode.D))
        {
            animator.SetBool("isWalking", false);
            animator.SetBool("isRunning", false);
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            animator.SetBool("idDefend", true);
        }
        if (Input.GetKeyUp(KeyCode.Space))
        {
            animator.SetBool("idDefend", false);
        }

        if (Input.GetKey(KeyCode.Mouse0))
        {
            animator.SetBool("attack1", true);
        }
        if(Input.GetKeyUp(KeyCode.Mouse0))
        {
            animator.SetBool("attack1", false);
        }

        if (Input.GetKey(KeyCode.Mouse1))
        {
            animator.SetBool("attack2", true);
        }
        if (Input.GetKeyUp(KeyCode.Mouse1))
        {
            animator.SetBool("attack2", false);
        }
    }
}
