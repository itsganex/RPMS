document.addEventListener("submit",e=>{
 const f=e.target;if(!(f instanceof HTMLFormElement))return;
 for(const el of f.querySelectorAll("[required]")){if(!el.value.trim()){el.focus();el.setCustomValidity("This field is required.");el.reportValidity();el.setCustomValidity("");e.preventDefault();return}}
 const pct=f.elements.percentage;if(pct&&pct.value&&(Number(pct.value)<0||Number(pct.value)>100)){pct.setCustomValidity("Percentage must be between 0 and 100.");pct.reportValidity();pct.setCustomValidity("");e.preventDefault()}
 const backlog=f.elements.backlog_count;if(backlog&&Number(backlog.value)<0){backlog.setCustomValidity("Backlog count cannot be negative.");backlog.reportValidity();backlog.setCustomValidity("");e.preventDefault()}
 const min=f.elements.min_package,max=f.elements.max_package;if(min&&max&&min.value&&max.value&&Number(min.value)>Number(max.value)){max.setCustomValidity("Maximum package must be at least minimum package.");max.reportValidity();max.setCustomValidity("");e.preventDefault()}
});
