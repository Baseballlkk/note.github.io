# Circulation and Vorticity
## Introduction
### Definition
1. Circulation
    * **Physical Meaning**
Degree of fluid rotating in limited region, a scalar macroscopic quantity.
    * **Expression**
$$C = \oint_l \vec{v} \cdot d\vec{l}$$

2. Vorticity
    * **Physical Meaning**
    Degree of rotating of small increment of fluid, a vector microscopic quantity.
    * **Expression**
    $$\zeta = \lim_{A\rightarrow 0}\frac{C}{A}$$

## Kelvin Circulation Theorem
### Derivation
By momentum equation in absolute coordinate:
$$\frac{D_a \vec{v_a}}{Dt} = -\frac{1}{\rho}\nabla p-\nabla \Phi$$

By the definition of circulation:
$$C = \oint_L \vec{v}\cdot d\vec{l}$$

Computing the Changing rate of circulation:
The left side of the momentum equation looks like
$$\oint_L \frac{D_a \vec{v_a}}{Dt}\cdot d\vec{l} = \oint_L (\frac{D}{Dt}(\vec{v_a}\cdot d\vec{l})-\vec{v_a}\cdot d\vec{v_a})$$

The right part of the equation looks like:
$$\oint_L-\frac{1}{\rho}\nabla p\;d\vec{l}+\oint_L-\nabla \Phi\;d\vec{l}$$

Since $\vec{v_a}\cdot d\vec{v_a}$ and $\nabla \Phi$ are independent from the route, the equation can be written in:
$$\frac{DC_a}{Dt} = \frac{D_a }{Dt}\oint_L \vec{v_a}\cdot d\vec{l} = \oint_L-\frac{1}{\rho}\nabla p\;d\vec{l}$$

The righter term is called solenoidal term.
This is Kelvin Circulation Theorem.

### Baroclinic unstable
By Kelvin Circulation Theorem, if the density of parcel is only depend on pressure, then the solenoidal term is 0, which means that the absolute circulation isn't change.
In another words, the circulation is stable.
In this case, the condition is called barotropic atmosphere.
However, if the density $\rho=\rho(p, T)$, the solenoidal term is not 0.
This means that the circulation is relatively unstable.
In this case, the condition is called baroclinic atmosphere or **baroclinic unstable**. 

### Example: Land-Sea Breeze
Land-sea breeze is a phenomenon which is common seen in area close to coastline.
The main cause of  this phenomenon is baroclinic unstable.
Consider there is two isobaric surface: $p_s$ and $p$, temperature $T_w, T_c$
By Kelvin Circulation Theorem:
$$\frac{DC_a}{Dt} =\oint_L-\frac{1}{\rho}\nabla p\;d\vec{l}$$

To calculate the line integral on the right-hand side:
$$\oint_L-\frac{1}{\rho}\nabla p\;d\vec{l} = \oint_L-\frac{RT}{p}\;dp$$

$$\Rightarrow \frac{DC_a}{Dt} = Rln(\frac{p_s}{p})(T_w-T_c)$$

In this expression, it is clear that the changing rate of absolute circulation is positive.
Therefore, the circulation is positive.
Which means that the circulation would rise in the warm pool, doing counter-clockwise motion.

By definition, the land-sea breeze need to flow with the speed 3 kts, we can thus build up the equation like below:
$$\frac{DC_a}{Dt} = Rln(p_s/p)(T_x-T_c)$$

Average of speed:
$$<v> = \frac{C_a}{\oint_L d\vec{l}}$$

$$<a>= \frac{D}{Dt}\frac{C_a}{\oint_L d\vec{l}} = Rln(p_s/p)(T_x-T_c)/(2(h+L))$$

Therefore, in order to form land-sea breeze, at least $(3(h+L))/(Rln(p_s/p)(T_x-T_c))$ seconds is needed.

## Bjerknes Circulation Theorem
Absolute circulation is constructed by planetary circulation and relative circulation, or written in expression:
$$C_a = C_e+C$$

By the definition of circulation:
$$C_e = \oint_L \vec{v_e}\cdot d\vec{l} = \oint_L (\vec{\Omega}\times\vec{r})\cdot d\vec{l}$$

By Stoke's Theorem:
$$C_e = 2A\Omega sin\phi $$

Therefore, by Kelvin Circulation Theorem, Changing rate of relative circulation can be written in:
$$\frac{DC}{Dt} = \oint_L-\frac{1}{\rho}\nabla p\;d\vec{l}-2\Omega\frac{DA_e}{Dt}$$

$$\Rightarrow C_2-C_1 = -2\Omega(A_2sin\phi_2-A_1sin\phi_1)$$

Via the expression, relative circulation would be affected by the change of area and latitude.

## Vorticity
By the definition of vorticity:
$$\zeta\equiv \lim_{A\rightarrow 0}\frac{C}{A}$$

$$\Rightarrow \zeta = (\nabla\cdot \vec{v})\cdot \hat{n} = \frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}$$

By this definition, absolute vorticity ($\eta$), planetary vorticity (f) can also be asked.
Especially planetary vorticity, its value will the same as Coriolis constant.
Relation between these vorticity like below:
$$\eta = f+\zeta$$

### Vorticity in nature coordinate
Considering a little section of curve isobaric line, with angle $\delta \beta\rightarrow 0$, curvature radius $R_s$.
Consider a circulation is formed between the two lines.
By the definition of circulation:
$$C = \oint_L \vec{v}\cdot d\vec{l}$$

$$= v\cdot(\delta s+d(\delta s))-(v+\delta v)\cdot \delta s$$

$$=v\cdot (\delta s+\delta \beta\;\delta n)-(v+\frac{\partial v}{\partial n}\delta n)\cdot \delta s$$

$$=v\;\delta n\;\delta \beta-\frac{\partial v}{\partial n}\delta n\cdot \delta s$$

$$=\delta n\; \delta s\;(-\frac{\partial v}{\partial n}+\frac{v}{R_s})$$

By the definition of vorticity:
$$\zeta \equiv \lim_{A\rightarrow 0} \frac{C}{A}$$

$$=\lim_{\delta n, \delta s\rightarrow 0} \delta n\; \delta s\;(-\frac{\partial v}{\partial n}+\frac{v}{R_s})/(\delta n\; \delta s)$$

$$=-\frac{\partial v}{\partial n}+\frac{v}{R_s}$$

This is the vorticity in nature coordinate.
The $-\frac{\partial v}{\partial n}$ is shear vorticity, $\frac{v}{R_s}$ is curvature vorticity.

## Potential Vorticity
### Purpose 
By Kelvin Circulation Theorem, in barotropic atmosphere, absolute vorticity is a conservative quantity. 
In order to define a quantity that is conservative in baroclinic atmosphere, potential vorticity is thus developed.

### Definition
$$PV = -g\frac{\delta \theta}{\delta p}(\zeta_\theta+f)$$

<font color = #00f>

<pf.>
By the definition of potential temperature:
$$\theta = T(\frac{p_0}{p})^{\frac{R_d}{C_p}}$$

By ideal gas law:
$$\Rightarrow \theta = \frac{p}{\rho R_d}(\frac{p_0}{p})^{\frac{R_d}{C_p}}$$

$$\Rightarrow \rho = p^{\frac{C_v}{C_p}}(R\theta)^{-1}p_0^{\frac{R_d}{C_p}}$$

if the parcel flow along isentropic surface, $\rho$ will only depends on pressure (like barotropic).
Also, by this property, using Kelvin Circulation Theorem:
$$\frac{DC_a}{Dt} = \frac{D}{Dt}(C_\theta+2\Omega sin\phi\; \delta A) = 0$$

$$\Rightarrow (\zeta_\theta+f)\delta A = const.$$

Consider the definition of pressure:
$$-\delta p = \frac{g\delta M}{\delta A}$$

$$\Rightarrow \frac{\delta M}{\delta \theta} = const.$$

By using this two equations:
$$(\zeta_\theta+f)\delta A = const.$$

$$\Rightarrow -(\zeta_\theta+f)\frac{g}{\delta p}\delta M = const.$$

$$\Rightarrow -g\frac{\delta \theta}{\delta p}\frac{\delta M}{\delta \theta}(\zeta_\theta+f) = const.$$

Since $\frac{\delta M}{\delta \theta} = const.$:
$$-g\frac{\delta \theta}{\delta p}(\zeta_\theta+f) = const. = PV$$

in which $\frac{\delta p}{\delta \theta}$ is quantity of effective depth.
</font>

### Rossby potential vorticity conservation law
By the definition of vorticity, term $\frac{\delta \theta }{\delta p}$ can be regarded as depth of atmosphere.
Transferring into altitude coordinate, it can be written in:
$$\frac{\zeta_\theta+f}{h} = const.$$

This equation is also called **Rossby potential vorticity conservation law**.

Considering conditions below:
#### No terrain
Generally, if there is no terrain effect, $h$ can be approximated as a constant.
Now, firstly consider easterly wind. 
If the flow turn counter-clockwise, $\zeta_\theta >0$. Also, $f$ increase, the total amount is increasing, not conservative.
If the flow turn clockwise, $\zeta_\theta <0$, and $f$ decrease, then the total is decreasing, not conservative.

Next, considering the westerly wind, if the parcel flow clockwise, $\zeta_\theta <0$, $f increasing$, the total is 0, conservative.
If the wind flow counter-clockwise, $\zeta_\theta >0$, $f$ is decreasing, conservative.

#### 
