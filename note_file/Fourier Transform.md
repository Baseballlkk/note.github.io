###### tags: `Application Mathematics`
# Fourier Transform
## Orthogonal function
### Orthogonal in discrete system
* **inner product**
$$(f_1(x), f_2(x)) = \Sigma_n f_1[n]\; f_2[n]$$
* **orthogonal**
$$(f_1(x), f_2(x))=0$$
***
### Orthogonal in continuous function
* **inner product**
$$(f_1(x), f_2(x)) = \int_a^b\; f_1(x)f_2^*(x)\; dx$$
$f_2^*(x)$ means the conjugation of $f_2(x)$
    + properties
        1. $(f_1, f_2) = (f_2, f_1)^*$
        2. $(kf_1, f_2) = k(f_1, f_2)$
        3. if and only if $f=\vec{0}$, $(f, f) = 0$
        4. $(f_1+f_2, g) = (f_1, g)+(f_2, g)$

* **Orthogonal function**
if $$(f_1, f_2) = \int_a^b f_1(x) f_2^*(x)\;dx = 0$$
then $f_1, f_2$ is orthogonal to each other.
    + special case
    any even function and any odd function must be orthogonal to each other within $[-a, a]$

* **Orthogonal set**
In $\phi_1(x), \phi_2(x), \phi_3(x), ..., \phi_n(x)$, if $(\phi_m(x), \phi_n(x))=0 \; (m!=n)$ in $[a, b]$
then the set of function is called **orthogonal set**.
***

### Orthonormal function
* **square norm**
$$||f(x)||^2 = (f(x), f^*(x)) = \int_a^b f(x)f^*(x)\; dx$$
* **norm**
$$||f(x)|| = (f(x), f^*(x))^{1/2} = \sqrt{\int_a^b f(x)f^*(x)\; dx}$$
* **orthonormal**
Considering a set of orthogonal function, and norm of each function included in it equals to 1, then the set of function is called **orthonormal set**.
* **normalization**
If wanna transfer the orthogonal set into orthonormal set,
dividing norm of each element function in the set is the method. 
This process is called **normalization**.
* **complete**
This property can be examined piecewise.
If any function within [a, b] can be represented by linear combination of a  set of function, then the set of function is called **complete**.
* **orthogonal series expension**
Considering $\phi(x)$ is a set of complete and orthogonal function, then any function within the interval can be written in:
$$f(x) = \Sigma_{n=0}^\infty \; c_n\; \phi_n(x)$$

    this expression is called orthogonal series expension.

* **Generalize fourier series**
Considering
$$\int_a^b f(x)\phi_n^*(x)\; dx = \Sigma_{m=0}^\infty c_m\int_a^b \phi_m(x)\phi_n^*(x)\; dx = c_n \int_a^b \phi_n(x)\phi_n^*(x) \; dx$$$$\Rightarrow c_n = \frac{\int_a^b f(x)\phi_n^*(x)\; dx}{\int_a^b \phi_n(x)\phi_n^*(x) \; dx}$$

    If the $\phi(x)$ is orthonormal function, then:
    $$c_n = \int_a^b f(x)\phi_n^*(x)\; dx$$
    
    Since that the norm of the orthomormal function is 1. 
***
### Weighting function
* **weighting function**
Emphasize structure of features, making the importance of different value different.
* **inner product**
$$(f_1, f_2) = \int_a^b w(x)f_1(x)f_2(x)\; dx$$

    all the properties need to time $w(x)$
***
## Fourier Series
### Trigonomatric function
Using $cos(\frac{n\pi}{p}x)$ and $sin(\frac{n\pi}{p}x)$ to form set of function.
Based on the definition before, this set is orthogonal and complete.

### Fourier Series
* **Definition**
$$f(x) = \frac{a_0}{2}+\Sigma_{n=1}^\infty (a_ncos(\frac{n\pi}{p}x)+b_nsin(\frac{n\pi}{p}x))$$

$$a_n = \frac{1}{\pi}\int_{-p}^p f(x)cos(\frac{n\pi}{p}x)\; dx$$

$$b_n = \frac{1}{\pi}\int_{-p}^p f(x)sin(\frac{n\pi}{p}x)\; dx$$

* **Physical meaning**
Transform the input signal into frquency analysis

* **limitation**
    + if the input function is not continuous, it is not always true to establish Fourier series.
There is a little bit fixing:
$$f(a-)=y_1, f(a+)=y_2, \;f(a)\frac{y_1+y_2}{2}$$
    + Fourier Series Expension
    the function that is procedured by Fourier series, the function will be forced to be periodic function with period $2\pi$.
    More advance method will be introduced later.

### Partial Sum
The Fourier series is the sum of infinity sum.
if $lim_{N\rightarrow \infty}\Sigma_{n=1}^N$, then the sum is approach Fourier series.
***
## Fourier Cosine and Sine Series
### Even and Odd function
if $f(x)=f(-x)$, the function is called even function.
if $f(x)=-f(-x)$, the function is called odd function.

### properties
even function: e
odd function : d
* e*e=e
* o*o=e
* e$\pm$e=e
* o$\pm$o=o
### Fourier cosine and sine series
* **cosine series**
$$f(x)=\frac{a_0}{2}+\Sigma_{n=1}^\infty a_ncos(\frac{n\pi}{p}x)$$

$$a_0 = \frac{2}{p}\int_0^pf(x)dx$$

$$a_n = \frac{2}{p}\int_0^pf(x)cos(\frac{n\pi}{p}x)\; dx$$
* **sine series**
$$f(x)=\Sigma_{n=1}^\infty b_n sin(\frac{n\pi}{p}x)$$

$$b_n = \frac{2}{p}\int_0^p f(x)sin(\frac{n\pi}{p}x)$$
***
## Application
### Half-range expansion
Only knowing half of the behavior of function.
Like: $f(x), \; 0<x<L$
if there are three ways to do expansion:
* **cosine series**
get an even function, substitute $p\rightarrow L$
* **sine series**
get an odd function, substitute $p\rightarrow L$
* **Fourier series**
get an periodic function

### paticular solution
for a $n-degree$ ODE, if the forcing is a periodic function, then this method is useful.
Step 1: transfer forcing function into Fourier series
Step 2: use basic method to suppose particular solution
Step 3: solve the ODE

***
## Fourier Integral
### Adventage
Fourier series can only solve problem of periodic function, but many signal are not obvious enough to show their property as a periodic function.
Therefore, if the function is not periodic, its period can be regarded as infinity. 
In this interpretation, Fourier integral can solve problems that Fourier series can't solve.

### Expression
$$f(x) = \frac{1}{\pi}\int_0^{\infty} [A(\alpha)cos(\alpha x)+B(\alpha)sin(\alpha x)]\; d\alpha$$

in which:
$$A(\alpha) = \int_{-\infty}^{\infty} f(x)cos(\alpha x)\; dx$$ $$B(\alpha) = \int_{-\infty}^{\infty} f(x)sin(\alpha x)\; dx$$

### Fourier cosine & sine integral
* **Fourier cosine integral**
When the function is even or has its interval $[0, \infty)$, the function can use cosine integral to analysis.
$$f(x) = \frac{2}{\pi}\int_{-\infty}^{\infty} A(\alpha)cos(\alpha x)\;d\alpha$$ $$A(\alpha) = \int_0^{\infty} f(x)cos(\alpha x)\; dx$$
* **Fourier sine integral**
When the function is odd or has its interval $[0, \infty)$, the function can use sine integral to analysis.
$$f(x) = \frac{2}{\pi}\int_{-\infty}^{\infty} B(\alpha)sin(\alpha x)\;d\alpha$$ $$A(\alpha) = \int_0^{\infty} f(x)sin(\alpha x)\; dx$$

### Sufficient Condition of Fourier integral
Consider a function $f$ has its fourier integral function:
$$\int_{-\infty}^{\infty}A(\alpha) cos(\alpha x) \; dx$$
Since $A(\alpha) cos(\alpha x)\le |A(\alpha) cos(\alpha x)|\le |A(\alpha)|$, we can thus get:
$$\int_{-\infty}^{\infty} A(\alpha) cos(\alpha x)\; d\alpha \le \int_{-\infty}^{\infty} |A(\alpha)|\; d\alpha$$

If the absolute integral converges, the Fourier integral of $f(x)$ exists.
This condition is called absolute integralable, which is a sufficient condition of Fourier integral.

### Partial integral
If only wanna consider specific realm of phenomenon, partial integral can help us to do analysis.
Its form is transfering $\infty$ to the boundary acquired.
Aside from this, it is almost the same as Fourier integral.

### Complex Form of Fourier Integral
Main expression looks like below:
$$f(x) = \frac{1}{\pi}\int_{-\infty}^{\infty}C(\alpha)e^{-j\alpha x} \; d\alpha$$

in which:
$$C(\alpha) = \int_{-\infty}^{\infty}f(x)e^{j\alpha x} \; dx$$


<font color=#00f>
<pf.>

By the definition of Fourier integral:
$$f(x) = \frac{1}{2\pi}\int_{0}^{\infty}(A(\alpha)cos(\alpha x)+B(\alpha)sin(\alpha x))\; d\alpha$$ $$\Rightarrow f(x)=\frac{1}{\pi}\int_0^{\infty}\int_{-\infty}^{\infty}f(t)[cos(\alpha t)cos(\alpha x)+sin(\alpha t)sin(\alpha x)]\;dt\; d\alpha$$ $$\Rightarrow f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(t)cos(\alpha(t-x))\;dt\; d\alpha$$

$$\because \int_{-\infty}^{\infty}f(t)sin(\alpha(t-x))\; d\alpha = 0$$ $$\therefore f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(t)[cos(\alpha(t-x))+jsin(\alpha(t-x))]\;dt\; d\alpha$$ $$f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(t)e^{j\alpha (t-x)}\;dt\; d\alpha$$ $$f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} [\int_{-\infty}^{\infty}f(t)e^{j\alpha t}\;dt]e^{-j\alpha x}\; d\alpha$$
</font>

***
## Fourier transform
Complex form is fourier transform.
### Expression
$$\hat f(\xi) = \int_{-\infty}^{\infty} f(x)e^{j\alpha x} \; dx$$

in which $\xi$ is frquency.

### Definition
* **Fourier transform**
$$\hat f(\xi) = \int_{-\infty}^{\infty} f(x)e^{j\alpha x} \; dx$$
* **inverse Fourier transform**
$$f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat f(\xi)e^{-j\alpha x}\; d\alpha$$
* **Fourier sine transform**
$$\hat f_s(\xi) = \int_{0}^{\infty} f(x)sin(\alpha x) \; dx$$
* **inverse Fourier sine transform**
$$f(x) = \frac{2}{\pi}\int_{0}^{\infty} \hat f(\xi)sin(\alpha x)\; d\alpha$$
* **Fourier cosine transform**
$$\hat f_c(\xi) = \int_0^{\infty} f(x)cos(\alpha x)\; dx$$
* **inverse Fourier cosine transform**
$$f(x) = \frac{2}{\pi}\int_{0}^{\infty} \hat f_c(\xi)cos(\alpha x)\; d\alpha$$