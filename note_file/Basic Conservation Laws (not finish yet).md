###### tags: `Atmospheric Dynamics`
# Basic Conservation Laws (not finish yet)
## Total differentiation
### Transform between local observation and global observation
Consider a quantity $A(x, y, z, t)$, its small change $\delta A$ can use Taylor's expansion to written in:
$$\delta A = \frac{\partial A}{\partial x} \; \delta x+ \frac{\partial A}{\partial y} \; \delta y+\frac{\partial A}{\partial z} \; \delta z+\frac{\partial A}{\partial t} \; \delta t+O(\delta x^2, \delta y^2, \delta z^2, \delta t^2)$$

Ignoring high order terms, then dividing $\delta t$, can get:
$$\frac{\delta A}{\delta t} = \frac{\partial A}{\partial x} \; \frac{\delta x}{\delta t}+ \frac{\partial A}{\partial y} \; \frac{\delta y}{\delta t}+\frac{\partial A}{\partial z} \; \frac{\delta z}{\delta t}+\frac{\partial A}{\partial t} $$

Consider $\lim_{\delta t \rightarrow 0}\frac{\delta A}{\delta t} = \frac{DA}{Dt}$
$$\frac{DA}{Dt} = \frac{\partial A}{\partial t}+u\frac{\partial A}{\partial x}+v\frac{\partial A}{\partial y}+w\frac{\partial A}{\partial z}$$
$$=\frac{\partial A}{\partial t}+\vec{V}\cdot \nabla A$$

This expression shows that the changing rate of local observer is consisted of changing as time and advection term.
Advection term $-\vec{V}\cdot \nabla A$ means that the wind flow from low value area to hugh value area.
When the advection term is negative, it is called **cool advection**.

***

### Total differentiation of vector property in rotating coordination
Making $\vec{A}$ as a vector property, it can be shown as:
$$\vec{A} = A_x^\prime \; \hat{i^\prime}+A_y^\prime \; \hat{j^\prime}+A_z^\prime \; \hat{k^\prime}\; \;(in\;absolute\; coordination)$$

or
$$\vec{A} = A_x \hat{i}+A_y\hat{j}+A_z\hat{k}\;(in\; rotating \; system)$$

Consider total differentiation in absolute coordination:
$$\frac{D_a \vec{A}}{Dt} = \frac{DA_x}{Dt}\hat{i}+\frac{DA_y}{Dt}\hat{j}+\frac{DA_z}{Dt}\hat{k}+\frac{D_a\hat{i}}{Dt}A_x+\frac{D_a\hat{j}}{Dt}A_y+\frac{D_a\hat{k}}{Dt}A_z$$ 
$$\Rightarrow \frac{D_a \vec{A}}{Dt} = \frac{D\vec{A}}{Dt}+\frac{D_a\hat{i}}{Dt}A_x+\frac{D_a\hat{j}}{Dt}A_y+\frac{D_a\hat{k}}{Dt}A_z$$ 
$$\Rightarrow \frac{D_a \vec{A}}{Dt} = \frac{D\vec{A}}{Dt}+\vec{\Omega}\times \vec{A}$$
***
## Momentum equation in rotating system
Make $\vec{r}$ is position vector, its velocity:
$$\frac{D_a\vec{r}}{Dt} = \frac{D\vec{r}}{Dt}+\vec{\Omega}\times \vec{r}$$ 
$$\Rightarrow \vec{U_a} = \vec{U}+\vec{\Omega}\times \vec{r}$$

Calculating the absolute acceleration:
$$\frac{D_a\vec{U_a}}{Dt} = \frac{D\vec{U_a}}{Dt}+\vec{\Omega}\times \vec{U_a}$$ 
$$\Rightarrow \frac{D_a\vec{U_a}}{Dt} = \frac{D\vec{U}}{Dt}+2\vec{\Omega}\times \vec{U}-\Omega^2\vec{R}$$

By Newton's second law of motion:
$$\Sigma\vec{F} = \frac{D\vec{U}}{Dt}+2\vec{\Omega}\times \vec{U}-\Omega^2\vec{R}$$ 
$$\Rightarrow \frac{D\vec{U}}{Dt} = \Sigma \vec{F}+\Omega^2\vec{R}-2\vec{\Omega}\times \vec{U}$$

$\Sigma \vec{F}$ includes PGF, viscous force, grvatational force.
The complete form of momentum equation in rotating system:
$$\frac{D\vec{U}}{Dt} = -\frac{1}{\rho}\nabla p+\vec{F_r}+\vec{g}-2\vec{\Omega}\times \vec{U}$$

***
## Component equation of momentum equation in rotating system
By using product rule, $\frac{D\vec{U}}{Dt}$ can be seperated into:
$$\frac{D U_x}{Dt} = \frac{Du}{Dt}-\frac{uv\;tan\phi}{a}+\frac{uw}{a}$$ 
$$\frac{D U_y}{Dt} = \frac{Dv}{Dt}+\frac{u^2\;tan\phi}{a}+\frac{vw}{a}$$ 
$$\frac{D U_z}{Dt} = \frac{Dw}{Dt}-\frac{u^2+v^2}{a}$$

Considering $\vec{\Omega}=<0, cos\phi, -sin\phi>$, using cross product with velocity, Coriolis term can be written in:
$$-2\vec{\Omega}\times \vec{U} = <-2\Omega w\;cos\phi+2\Omega v\; sin\phi, -2\Omega u\; sin\phi, 2\Omega u\; cos\phi>$$

Based on the derivation above, momentum equation can be written in:
$$\frac{Du}{Dt}-\frac{uv\;tan\phi}{a}+\frac{uw}{a} = -\frac{1}{\rho}\frac{\partial p}{\partial x}+F_{rx}-2\Omega w\;cos\phi+2\Omega v\; sin\phi$$ 
$$\frac{Dv}{Dt}+\frac{u^2\;tan\phi}{a}+\frac{vw}{a}=-\frac{1}{\rho}\frac{\partial p}{\partial y}+F_{ry}-2\Omega u\; sin\phi$$ 
$$\frac{Dw}{Dt}-\frac{u^2+v^2}{a}=-\frac{1}{\rho}\frac{\partial p}{\partial z}+F_{rz}+2\Omega u\; cos\phi$$
***

## Scale Analysis of momentum equation
Considering horizontal term, and the result like below:
| physical meaning | dimension | scale|
|---|---|---|
|acceleration|$U^2/L$|$10^{-4}$|
|Coriolis (caused by horizontal wind)|$f_0 U$|$10^{-3}$|
|Coriolis (caused by vertical wind)|$f_0 W$| $10^{-6}$|
|curvature | $U^2/a$ | $10^{-5}$|
|PGF|$\frac{\delta P}{\rho L}$|$10^{-3}$|
|vicous force|$\frac{\nu U}{H^2}$|$10^{-12}$|

By the analysis above, the most important terms are PGF and Coriolis force caused by horizontal wind.

### Geostrophic approximation and geostrophic wind
By scale analysis, there is approximation expression:
$$-fv\approx -\frac{1}{\rho}\frac{\partial p}{\partial x}$$ 
$$fu\approx -\frac{1}{\rho}\frac{\partial p}{\partial y}$$

These two expression are called ***geostrophic approximation*** .
if the two expression be true (approximate -> equal), then the wind is called ***geostrophic wind***. Written in:
$$v_g = \frac{1}{\rho f}\frac{\partial p}{\partial x} \hat{j}$$ 
$$u_g = -\frac{1}{\rho f}\frac{\partial p}{\partial y} \hat{i}$$

These expressions can be written in vector form:
$$\vec{V_g} = \hat{k}\times \frac{1}{\rho f}\nabla p$$
### Rossby number
Since it is an approximaiton, needing an index to examine its validity.
Using the ratio of horizontal acceleration and Coriolis force, the its dimension would looks like:
$$R_o = \frac{U^2/L}{f_0U} = \frac{U}{f_0L}$$
If the number is smaller, the approximation is more valid.

### Hydrostatic Approximation
By hydrostatic equation:
$$\frac{dp}{dz}=-\rho g$$
Considering there is perturbation (much smaller than basic field), the field can be written in:
$$p(x, y, z, t) = p_0(z)+p^\prime (x, y, z, t)$$ 
$$\rho(x, y, z, t) = \rho_0(z)+\rho^\prime (x, y, z, t)$$

Bring these two feild into the hydrostatic equation, it can be simplified as:
$$-\frac{1}{\rho}\frac{\partial p}{\partial z} = -\frac{1}{\rho_0} [p^\prime g+\frac{\partial \rho^\prime}{\partial z}]$$

Examine the two term in the approximation:
$$\frac{p^\prime g}{\rho_0}\approx [\frac{\delta p}{\rho_0 H}]\approx 10^{-1} \;m/s^2$$ 
$$\frac{\partial \rho^\prime}{\rho_0 \partial z}\approx 10^{-1} \;m/s^2$$

By the analysis, we can get equation:
$$\frac{\partial p^\prime}{\partial z} = -\rho^{\prime} g$$